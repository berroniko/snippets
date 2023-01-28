from tqdm import tqdm
from time import sleep

def show_tqdm():
    """Example for using tqdm

    Loops show a progress meter - just byte wrapping any iterable with tqdm(iterable)
    """

    for i in tqdm(range(1000)):
        sleep(0.001)  # simulates execution of some lines of code


if __name__ == '__main__':
    show_tqdm()
