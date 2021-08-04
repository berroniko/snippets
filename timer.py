from datetime import datetime
import functools

def timer(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		start = datetime.now()
		res=func(*args, **kwargs)
		end = datetime.now()
		print('{} completed in {} sec'.format(func.__name__, end-start))
		return res
	return inner

@timer
def calc(n,exp):
	'''docstring of decorated function gets lost unless decorator uses wraps'''	
	y=sum([i**exp for i in range(n)])		
	return y

@timer
def calc_loop(n,exp):
	r=0
	for i in range(n):
		r+=i**exp
	return r

print(calc(999999,3))
print(calc.__doc__)
print(calc_loop(999999,3))

	

