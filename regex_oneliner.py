import re


string = 'abckeid_34.5'

res = re.search(r'(\d+)$', string)   # numbers at end of string

if res:
	print(res.group())
else:
	print('not found')
