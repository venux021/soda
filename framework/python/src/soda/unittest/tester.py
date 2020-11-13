import argparse
import json
import os.path
import signal
import subprocess
import sys
import time

from soda.unittest import diff, util

from subprocess import Popen, PIPE

framework_dir = os.environ['SODA_FRAMEWORK_DIR']
verbose = False
testcase_timeout = 5.0

class DataConfig:

    @classmethod
    def new(cls):
        return {
            'showArgs': True,
            'showResult': True,
            'skip': False
        }

    @classmethod
    def parse(cls, text):
        config = cls.new()
        text = text.strip()
        if text:
            c = json.loads(text)
            config.update(c)
        return config

def pstree(pid: int):
    pid_list = []
    def recursive(pid):
        res = subprocess.run(f'pgrep -P {pid}', shell=True, stdout=PIPE, encoding='utf-8')
        text = res.stdout.strip()
        if not text:
            return
        c_pids = []
        for cpid in text.split('\n'):
            cpid = cpid.strip()
            try:
                cpid = int(cpid)
                recursive(cpid)
                pid_list.append(cpid)
            except:
                pass
    recursive(pid)
    return pid_list

def kill_all_child_processes(ppid):
    for cpid in pstree(ppid):
        subprocess.run(f'kill -9 {cpid}', shell=True, stdout=PIPE, stderr=PIPE)
        time.sleep(0.01)

def build_test_object(lines):
    testobj = {}
    testobj['args'] = list(map(json.loads, lines[:-1]))
    if lines[-1] != '-':
        testobj['expected'] = json.loads(lines[-1])
    else:
        testobj['expected'] = None
    return testobj

def parse_input(fp):
    status = 0
    lines = []
    config = None
    for line in fp:
        line = line.strip()
        if status == 0:
            if line.startswith('#>>') or line.startswith('@>>'):
                config = DataConfig.parse(line[3:])
                status = 1
        elif status == 1:
            if line.startswith('#<<') or line.startswith('@<<'):
                yield (config, build_test_object(lines))
                status = 0
                lines = []
                config = None
            elif line and line[0] != '#':
                lines.append(line)

def run_python(srcfile, testobj):
    runner = f'{framework_dir}/python/run.sh'
    command = f'{runner} {srcfile}'
    return call_process(command, testobj)

def run_java(classname, testobj):
    if os.environ.get('SODA_JAVA_SERVER_MODE') == 'yes':
        command = f'{framework_dir}/java/run-client.sh {classname}'
    else:
        command = f'{framework_dir}/java/run.sh {classname}'
    return call_process(command, testobj)

def run_cpp(exefile, testobj):
    command = f'{framework_dir}/cpp/run.sh {exefile}'
    return call_process(command, testobj)

def run_scala(classname, testobj):
    if os.environ.get('SODA_SCALA_SERVER_MODE') == 'yes':
        command = f'{framework_dir}/scala/run-client.sh {classname}'
    else:
        command = f'{framework_dir}/scala/run.sh {classname}'
    return call_process(command, testobj)

def run_ruby(srcfile, testobj):
    command = f'{framework_dir}/ruby/run.sh {srcfile}'
    return call_process(command, testobj)

def call_process(command, testobj):
    datatext = json.dumps(testobj)
    return_code = None
    with Popen(command, shell=True, stdin=PIPE, stdout=PIPE, encoding='utf-8') as proc:
        try:
            outs, _ = proc.communicate(datatext, timeout=testcase_timeout)
        except:
            kill_all_child_processes(proc.pid)
            # outs, _ = proc.communicate()
            # proc.kill()
            raise Exception(f'Time Limit Exceeded')

        return_code = proc.returncode

    if return_code != 0:
        raise Exception(f'Sub process exit with {return_code}')

    try:
        return json.loads(outs)
    except:
        raise Exception(f'Invalid response: {outs}')

def run_code(lang, executable, testobj):
    if lang == 'python':
        return run_python(executable, testobj)
    elif lang == 'java':
        return run_java(executable, testobj)
    elif lang == 'cpp':
        return run_cpp(executable, testobj)
    elif lang == 'scala':
        return run_scala(executable, testobj)
    elif lang == 'ruby':
        return run_ruby(executable, testobj)
    else:
        raise Exception(f'Unsupported language: {lang}')

def execute(lang, executable, config, testobj):
    seq_number = testobj['id']
    print(f'**[{seq_number}]**')
    print(f'* {config["_test_file"]} <{config["_seq_in_file"]}>')

    if verbose:
        print('config:', json.dumps(config))
        print('request:', json.dumps(testobj))

    if config['showArgs']:
        print('input:')
        print(*list(map(json.dumps, testobj['args'])))

    if config['skip']:
        print('SKIP\n')
        return True

    try:
        response = run_code(lang, executable, testobj)
    except Exception as ex:
        print(f'Error: {ex}')
        return False

    if verbose:
        print('response:', json.dumps(response))

    #if not response['finished']:
    #    print('not finished due to internal error')
    #    reason = response.get('reason', '')
    #    if reason:
    #        print('Reason:', reason)
    #    return

    if not response['success']:
        util.print_in_red_color('TEST FAILED')
        res = response['result']
        expected = testobj['expected']
        if expected is not None:
            if res is None:
                print('Error: result is null')
                return False

            print('expected:', json.dumps(expected))
            print('result:', json.dumps(res))

            if type(expected) != type(res):
                print('Error: result and expected is not the same type')
                return False

            if isinstance(res, list):
                diff.with_list(expected, res)
            else:
                info = f'Wrong answer {json.dumps(res)}, but {json.dumps(expected)} expected'
                print(info)
        else:
            info = f'Wrong answer {json.dumps(res)}'
            print(info)
        return False

    util.print_in_green_color('SUCCESS')
    if config['showResult']:
        print('output:')
        print(json.dumps(response['result']))

    print('----')
    elapse = response['elapse']
    print(f'{elapse:.3f} ms\n')
    return True

def main():
    parser = argparse.ArgumentParser(prog='soda')

    parser.add_argument('language')
    parser.add_argument('exefile')
    parser.add_argument('--testcase', default='test_data')
    parser.add_argument('--delim', default=',')
    parser.add_argument('--verbose', action='store_true', default=False)
    parser.add_argument('--timeout', default=5.0, type=float)

    args = parser.parse_args()
    # print(args)

    language = args.language
    executable = args.exefile
    input_files = args.testcase.split(args.delim)

    global verbose
    verbose = args.verbose

    if not input_files:
        input_files = ['test_data']

    timeout = max(2.0, args.timeout)
    timeout = min(10.0, timeout)
    global testcase_timeout
    testcase_timeout = timeout

    counter = 0
    for infile in input_files:
        seq_in_file = 0
        with open(infile, 'r') as fp:
            for config, testobj in parse_input(fp):
                seq_in_file += 1
                counter += 1
                testobj['id'] = counter
                config['_test_file'] = infile
                config['_seq_in_file'] = seq_in_file
                if not execute(language, executable, config, testobj):
                    return

if __name__ == '__main__':
    main()

