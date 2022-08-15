from tqdm import tqdm
from time import sleep

"""
Example for using tqdm
Instantly make loops show a smart progress meter - just wrap any iterable with tqdm(iterable)
"""

r = 0
for i in tqdm(range(1000)):
    sleep(0.001)
    r += i**2

print(r)
