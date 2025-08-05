class MockConfig:
    def printer(self):
        return MockPrinter()

class MockPrinter:
    def ln(self, *args, **kwargs):
        print('\n')

    def textln(self, *args, **kwargs):
        print(*args, **kwargs)

    def text(self, *args, **kwargs):
        print(*args, end='', **kwargs)

    def cut(self, *args, **kwargs):
        print('\n')

