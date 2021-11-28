from functools import lru_cache
	
@lru_cache()
def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
		

@lru_cache()
def fact(n):
	return n * factorial(n-1) if n else 1


for i in range(0, 10):
	print(i, factorial(i))
