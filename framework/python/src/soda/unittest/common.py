class UnitTestRequest:

    def __init__(self, obj):
        self.obj = obj

    @property
    def answer(self):
        return self.obj['answer']

    @property
    def args(self):
        return self.obj['args'][:]

    @property
    def id(self):
        return self.obj['id']

    def arg(self, index):
        return self.obj['args'][index]
