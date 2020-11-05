import json
import sys
import time

from soda.unittest.codec import CodecFactory

class JobEntry:

    @staticmethod
    def run(*, 
            cls, method: str, arg_types, ret_type, 
            validate_by_object=False, 
            object_validator=None, 
            serial_validator=None):
        jspec = JobSpec()
        jspec.cls = cls
        jspec.method = method
        jspec.arg_types = arg_types
        jspec.ret_type = ret_type
        jspec.validate_by_object = validate_by_object
        jspec.object_validator = object_validator
        jspec.serial_validator = serial_validator
        
        runner = JobRunner()
        runner.run(jspec)

class InputData:

    def __init__(self, obj):
        self.obj = obj

    @property
    def expected(self):
        return self.obj['expected']

    @property
    def id(self):
        return self.obj['id']

    @property
    def args(self):
        return self.obj['args'][:]

    def arg(self, index):
        return self.obj['args'][index]

class JobSpec:
    pass

class JobRunner:

    def run(self, jbs: JobSpec) -> None:
        input_data = InputData(json.load(sys.stdin))
        args = (CodecFactory.create(t).decode(a) for t, a in zip(jbs.arg_types, input_data.args))

        method = getattr(jbs.cls, jbs.method)
        obj = jbs.cls()

        start = time.time()
        res = method(obj, *args)
        end = time.time()

        serial_res = CodecFactory.create(jbs.ret_type).encode(res)
        elapse = end - start

        resp = {
            'id': input_data.id,
            'result': serial_res,
            'elapse': elapse
        }

        success = True
        if input_data.expected is not None:
            if jbs.validate_by_object:
                vf = jbs.object_validator or (lambda x, y: x == y)
                expc = CodecFactory.create(jbs.ret_type).decode(input_data.expected)
                success = vf(res, expc)
            else:
                vf = jbs.serial_validator or (lambda x, y: x == y)
                success = vf(serial_res, input_data.expected)

        resp['success'] = success

        print(json.dumps(resp))

