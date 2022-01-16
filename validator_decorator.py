import functools


def ensure_positive(index):
    "checks if the argument at position 'index' of the function complies with condition in line 8"

    def validator(func):
        @functools.wraps(func)
        def inner(*args):
            if args[index] < 0:  # the condition to be validated
                raise ValueError(
                    f'The {index}. argument of function "{func.__name__}" must be positiv, but has the value: {args[index]}'
                )
            return func(*args)

        return inner

    return validator


def ensure_integer(index):
    "checks if the argument at position 'index' of the function complies with condition in line 22"

    def validator(func):
        @functools.wraps(func)
        def inner(*args):
            if not type(args[index]) == int:  # the condition to be validated
                raise ValueError(
                    f'The {index}. argument of function "{func.__name__}" must be type int,'
                    f' but is: {type(args[index])}'
                )
            return func(*args)

        return inner

    return validator


if __name__ == '__main__':
    @ensure_integer(index=0)
    @ensure_positive(index=1)
    def n_times_root(n, x):
        import math
        return n * math.sqrt(x)


    print(n_times_root(1, -3))
