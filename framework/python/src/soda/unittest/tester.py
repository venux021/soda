import argparse
import json
import os.path
from subprocess import Popen, PIPE
import sys

framework_dir = os.environ['SODA_FRAMEWORK_DIR']

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
            if line.startswith('#>>'):
                config = DataConfig.parse(line[3:])
                status = 1
        elif status == 1:
            if line.startswith('#<<'):
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

    if config['showArgs']:
        print('input:')
        print(*list(map(json.dumps, testobj['args'])))

    if config['skip']:
        print('SKIP\n')
        return

    response = run_code(lang, exefile, testobj)
    if response is None:
        raise Exception('Error: unabled to execute test')

    #if not response['finished']:
    #    print('not finished due to internal error')
    #    reason = response.get('reason', '')
    #    if reason:
    #        print('Reason:', reason)
    #    return

    if not response['success']:
        res = response['result']
        expected = testobj['expected']
        if expected is not None:
            info = f'Wrong answer {res}, but {expected} expected'
        else:
            info = f'Wrong answer {res}'
        raise Exception(info)
    elif config['showResult']:
        print('output:')
        print(json.dumps(response['result']))

    print('----')
    elapse = response['elapse']
    print(f'{elapse:.3f} ms\n')

def main():
    parser = argparse.ArgumentParser(prog='soda')

    parser.add_argument('language', choices=['python','java','cpp'])
    parser.add_argument('exefile')
    parser.add_argument('data_files', nargs=argparse.REMAINDER)

    args = parser.parse_args()

    language = args.language
    exefile = args.exefile
    input_files = args.data_files

    if not input_files:
        input_files = ['test_data']

    counter = 0
    for infile in input_files:
        with open(infile, 'r') as fp:
            for config, testobj in parse_input(fp):
                counter += 1
                testobj['id'] = counter
                execute(language, exefile, config, testobj)

if __name__ == '__main__':
    main()
