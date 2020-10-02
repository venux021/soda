import argparse
import json
import os.path
from subprocess import Popen, PIPE
import sys

from soda.unittest import diff, util

framework_dir = os.environ['SODA_FRAMEWORK_DIR']
verbose = False

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

def run_java(classfile, testobj):
    command = f'{framework_dir}/java/run.sh {classfile}'
    return call_process(command, testobj)

def run_cpp(exefile, testobj):
    command = f'{framework_dir}/cpp/run.sh {exefile}'
    return call_process(command, testobj)

def call_process(command, testobj):
    datatext = json.dumps(testobj)
    with Popen(command, shell=True, stdin=PIPE, stdout=PIPE, encoding='utf-8') as proc:
        try:
            outs, _ = proc.communicate(datatext, timeout=5)
        except:
            proc.kill()
            outs, _ = proc.communicate()

    try:
        resultobj = json.loads(outs)
    except:
        resultobj = None
        print('Invalid output:', outs)

    #print(errs, file = sys.stderr)
    return resultobj

def run_code(lang, exefile, testobj):
    if lang == 'python':
        return run_python(exefile, testobj)
    elif lang == 'java':
        return run_java(exefile, testobj)
    elif lang == 'cpp':
        return run_cpp(exefile, testobj)
    else:
        raise Exception(f'Unsupported language: {lang}')

def execute(lang, exefile, config, testobj):
    seq_number = testobj['id']
    print(f'**[{seq_number}]**')

    if verbose:
        print('config:', json.dumps(config))
        print('request:', json.dumps(testobj))

    if config['showArgs']:
        print('input:')
        print(*list(map(json.dumps, testobj['args'])))

    if config['skip']:
        print('SKIP\n')
        return True

    response = run_code(lang, exefile, testobj)
    if response is None:
        print('Error: unabled to execute test')
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

    parser.add_argument('language', choices=['python','java','cpp'])
    parser.add_argument('exefile')
    parser.add_argument('--testcase', default='test_data')
    parser.add_argument('--verbose', action='store_true', default=False)

    args = parser.parse_args()
    print(args)

    language = args.language
    exefile = args.exefile
    input_files = args.testcase.split(':')

    global verbose
    verbose = args.verbose

    if not input_files:
        input_files = ['test_data']

    counter = 0
    for infile in input_files:
        with open(infile, 'r') as fp:
            for config, testobj in parse_input(fp):
                counter += 1
                testobj['id'] = counter
                if not execute(language, exefile, config, testobj):
                    return

if __name__ == '__main__':
    main()

