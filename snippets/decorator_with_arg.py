import random

"""How to build a constructor that takes an argument"""

# https://youtu.be/pr1xfd6oTwY

# as a pure decorator     _____________________
def power_of_2(func):
    def inner():
        return func() ** 2

    return inner

# decorator with argument ____________________
def power_of(exp):
    """decorator accepting and argument"""
    # the 'meta' decorator with argument becomes an extra layer on top
    def decorator(func):
        def inner():
            return func() ** exp

        return inner

    return decorator

if __name__ == '__main__':
    @power_of_2
    def rnd_odd():
        return random.choice([1, 3, 5, 7, 9])

    print(rnd_odd())

    @power_of(4)
    def rnd_even():
        return random.choice([2, 4, 6, 8])

    print(rnd_even())
