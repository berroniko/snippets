from tqdm import tqdm
from time import sleep


r = 0
for i in tqdm(range(1000)):
    sleep(0.002)
    r += i**2

print(r)
