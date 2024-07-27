from typing import Callable


# _________currying _________
# multiple arguments would require multiple nested levels

def multiply_setup(a: float) -> Callable:
    def multiply(b: float) -> float:
        return a * b

    return multiply


double: Callable = multiply_setup(2)
triple: Callable = multiply_setup(3)

print(multiply_setup(4)(5))

print(f'{double(5)=}')
print(f'{triple(5)=}')



# _________partials _________
# can handle multiple arguments

from functools import partial


def multiply_partial(a: float, b: float, name: str | None = None) -> float:
    if name is not None:
        print(f'\n{name} (a: {a}, b: {b})')

    return a * b


double_partial = partial(multiply_partial, 2)
triple_partial = partial(multiply_partial, b=3, name='triple')

print(f'{double_partial(5)=}')
print(f'{triple_partial(5)=}')
