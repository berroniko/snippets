import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def logged(func, *args, **kwargs):
    logger = logging.getLogger()

    def inner(*args, **kwargs):
        logger.debug('calling {} with args {}, kwargs {}'.format(func.__name__, args, kwargs))
        return func(*args, **kwargs)

    return inner


@logged
def bar(text):
    print('executing bar')
    print(text)


bar("hello")
