import re


def regex_oneliner(string):
    res = re.search(r'(\d+)$', string)  # numbers at end of string

    if res:
        return (res.group())
    else:
        print('not found')
        return None


if "__name__" == "__main__":
    string = 'abckeid_34.5'
    print(regex_oneliner(string))
