from abc import ABC, abstractmethod
import json
import sys
import time

class TestRequest:

    def __init__(self, obj):
        self.obj = obj

    @property
    def expected(self):
        return self.obj['expected']

    @property
    def args(self):
        return self.obj['args'][:]

    @property
    def id(self):
        return self.obj['id']

    def arg(self, index):
        return self.obj['args'][index]


class TestResponse:

    def __init__(self):
        self.obj = {}

    @property
    def result(self):
        return self.obj['result']

    @result.setter
    def result(self, r):
        self.obj['result'] = r


class JobTemplate(ABC):

    def run(self, req: TestRequest, resp: TestResponse) -> None:
        resp.result = self.serialize(self.execute(req, resp))

    @abstractmethod
    def execute(self, req: TestRequest, resp: TestResponse) -> 'ResultType':
        pass

    @abstractmethod
    def serialize(self, res: 'ResultType') -> 'ResultSerialType':
        pass

    @abstractmethod
    def validate(self, req: TestRequest, resp: TestResponse) -> bool:
        pass

class Runner:

    def run(self, job: JobTemplate) -> None:
        req = TestRequest(json.load(sys.stdin))
        resp = TestResponse()
        resp.obj['id'] = req.id

        start = time.time()
        res = job.run(req, resp)
        end = time.time()

        resp.obj['elapse'] = (end-start) * 1000

        if req.expected is not None:
            resp.obj['success'] = job.validate(req, resp)
        else:
            resp.obj['success'] = True

        print(json.dumps(resp.obj))

