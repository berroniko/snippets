import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def logged(func, *args, **kwargs):
    """
    Decorator to log the use of the decorated function
    """

    logger = logging.getLogger()

    def inner(*args, **kwargs):
        logger.debug('calling {} with args {}, kwargs {}'.format(func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return inner


if __name__ == '__main__':
    @logged
    def bar(text, test=5):
        print('executing bar')
        print(text)
        print(test)


    bar("hello", test=12)
