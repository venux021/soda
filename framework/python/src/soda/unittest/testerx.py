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
    new_lines = []
    for i in range(len(lines)):
        if lines[i].startswith('@'):
            # load from file
            filepath = lines[i][1:]
            with open(filepath, 'r') as fp:
                for L in fp:
                    if L.strip():
                        new_lines.append(L)
        else:
            new_lines.append(lines[i])
    lines = new_lines
    testobj = {}
    testobj['args'] = list(map(json.loads, lines[:-1]))
    if lines[-1] != '-':
        testobj['expected'] = json.loads(lines[-1])
    else:
        testobj['expected'] = None
    return testobj

def parse_input(fp):
    first_line = next(fp)
    if not first_line.startswith('#@braces'):
        with open(fp.name, 'r') as fp2:
            yield from parse_input_legacy(fp2)
            return

    status = 0
    lines = []
    config = None
    for line in fp:
        line = line.strip()
        if status == 0:
            if line.startswith('{'):
                status = 1
        elif status == 1:
            if not line or line[0] == '#':
                continue
            if line.startswith('}'):
                yield (config or DataConfig.parse(''), build_test_object(lines))
                status = 0
                lines = []
                config = None
            elif line[0] == '$':
                if line.startswith('$config:'):
                    config = DataConfig.parse(line[len('$config:'):])
            else:
                lines.append(line)

def parse_input_legacy(fp):
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

def call_process(command, testobj):
    datatext = json.dumps(testobj)
    return_code = None
    # DONOT capture stderr! Message from stderr should print to console
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
        print_err(f'Error: failed to run test case')
        print_err(f'<stdout>: {outs}')
        raise Exception(f'Sub process exit with {return_code}')

    try:
        return json.loads(outs)
    except:
        raise Exception(f'Invalid response: {outs}')

def execute(script, testname, script_args, config, testobj):
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
        command = f'{script} run {testname} {script_args}'
        response = call_process(command, testobj)
    except Exception as ex:
        print(f'Error: {ex}')
        return False

    if verbose:
        print('response:', json.dumps(response))

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

def print_err(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def main():
    parser = argparse.ArgumentParser(prog='soda')

    parser.add_argument('testname')
    parser.add_argument('--testcase')
    parser.add_argument('--delim', default=',')
    parser.add_argument('--verbose', action='store_true', default=False)
    parser.add_argument('--timeout', default=5.0, type=float)
    parser.add_argument('--script', required=True)
    parser.add_argument('-X', default='')

    args = parser.parse_args()

    testname = args.testname
    if args.testcase is None:
        input_files = [f'{testname.lower()}.input']
    else:
        input_files = args.testcase.split(args.delim)

    global verbose
    verbose = args.verbose

    if not input_files:
        print_err('No test case specified')
        sys.exit(2)

    timeout = max(2.0, args.timeout)
    # timeout = min(10.0, timeout)
    global testcase_timeout
    testcase_timeout = timeout

    script_args = args.X

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
                if not execute(args.script, testname, script_args, config, testobj):
                    sys.exit(3)

if __name__ == '__main__':
    main()

