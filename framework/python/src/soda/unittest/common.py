from abc import ABC, abstractmethod

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

