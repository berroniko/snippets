import re


def regex_oneliner(string):
    """short version of regex application
    extracts numbers at the end of an string.
    >>> regex_oneliner("asldkj1.23")
    '23'
    """
    res = re.search(r'(\d+)$', string)  # numbers at end of string

    if res:
        return res.group()
    else:
        return None


if "__name__" == "__main__":
    string = 'abckeid_34.5'
    print(regex_oneliner(string))
