from tkinter import *
from tkinter import filedialog


def get_folderpath(title="Select folder", initialdir=None):
    """returns the path of the selected folder"""
    root = Tk()
    root.withdraw()
    root.folderpath = filedialog.askdirectory(title=title, parent=root, initialdir=initialdir)
    root.update()

    return root.folderpath


def get_filename(title="Select file", filetypes=None, initialdir=None):
    """returns the filepath"""
    root = Tk()
    root.withdraw()
    root.filename = filedialog.askopenfilename(title=title, initialdir=initialdir, filetypes=filetypes)
    root.update()

    return root.filename


if __name__ == '__main__':
    f = get_folderpath()

    f_types = (
        ('text files', '*.txt'),
        ('pdf files', '*.pdf')
    )
    n = get_filename(filetypes=f_types, initialdir=f)

    print(n)
