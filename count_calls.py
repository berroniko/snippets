class CountCalls:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CountCalls
def test_func(x):
    return x ** 2


print(test_func(2))
print(test_func(6))
print(f'Nr of calls to test_func: {test_func.count}')
