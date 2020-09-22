import argparse
import json
import os.path
from subprocess import Popen, PIPE
import sys

self_path = os.path.dirname(os.path.realpath(__file__))
framework_path = os.path.abspath(self_path + '/..')

def usage():
    print('python3 testtool.py <srcfile> <inputfile>...')

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
        testobj['answer'] = json.loads(lines[-1])
    else:
        testobj['answer'] = None
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
            elif line:
                lines.append(line)

def run_python(srcfile, testobj):
    python_dir = framework_path + '/python'
    runner = f'{framework_path}/python/run.sh'
    command = f'{runner} {srcfile}'
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

def run_code(srcfile, testobj):
    if srcfile.endswith('.py'):
        return run_python(srcfile, testobj)

def execute(counter, config, srcfile, testobj):
    print(f'**[{counter}]**')

    if config['showArgs']:
        print('input:')
        print(*testobj['args'])

    if config['skip']:
        print('SKIP\n')
        return

    response = run_code(srcfile, testobj)
    if response is None:
        print('Error: unabled to execute test', file = sys.stderr)
        return

    #if not response['finished']:
    #    print('not finished due to internal error')
    #    reason = response.get('reason', '')
    #    if reason:
    #        print('Reason:', reason)
    #    return

    if not response['success']:
        res = response['result']
        answer = testobj['answer']
        if answer is not None:
            info = f'Wrong answer {res}, but {answer} expected'
        else:
            info = f'Wrong answer {res}'
        raise Exception(info)
    elif config['showResult']:
        print('output:')
        print(response['result'])

    print('----')
    elapse = response['elapse']
    print(f'{elapse:.3f} ms\n')

def main():
    parser = argparse.ArgumentParser(prog='soda')

    parser.add_argument('srcfile')
    parser.add_argument('data_files', nargs=argparse.REMAINDER)

    args = parser.parse_args()

    srcfile = args.srcfile
    input_files = args.data_files

    counter = 0
    for infile in input_files:
        with open(infile, 'r') as fp:
            for config, testobj in parse_input(fp):
                counter += 1
                testobj['id'] = counter
                execute(counter, config, srcfile, testobj)

if __name__ == '__main__':
    main()
