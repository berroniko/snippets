
class Test():
    def __init__(self, first_nr):
        self.first = first_nr
        self._result = None

    def calculation(self):
        print("calculating")
        self._result = self.first * 5
        return self._result


    @property
    def result(self):
        print("input property")
        if not self._result:
            self.calculation()
        return self._result


if __name__ == '__main__':

    t = Test(2)
    print(t.result)
    print(t.result)
    print(t.calculation())
