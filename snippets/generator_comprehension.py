import itertools

"""A generator expression might be endless. If the comprehension is written between (), python does not start
evaluating the expression immediately, the behaviour becomes lazy and is only executed when called
"""

res = (i ** 2 for i in itertools.count())

# range limits the loop to 5 iterations, it has no other purpose
for n, _ in zip(res, range(5)):
    print(n)
