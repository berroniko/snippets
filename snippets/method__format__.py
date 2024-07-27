class Book:
    """show the use of method __format__

    Any python type, not only a class, can be formatted with the method __format__
    For details see: `PEP 3101 <https://peps.python.org/pep-3101/#controlling-formatting-on-a-per-type-basis>`__

    It is also possible to define and name different formats that can be specified in f-strings
    """

    def __init__(self, title: str):
        self.title = title

    def __format__(self, spec) -> str:
        match spec:
            case 'caps':
                return self.title.upper()
            case 'lower':
                return self.title.lower()
            case _:
                raise ValueError(f'unknown spec for Book()')


def main():
    book = Book('Test title')

    print(f'{book:caps}')
    # TEST TITLE

    print(f'{book:lower}')
    # test title


if __name__ == '__main__':
    main()
