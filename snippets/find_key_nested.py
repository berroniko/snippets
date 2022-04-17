import json
import pprint


#  https://stackoverflow.com/questions/9807634/find-all-occurrences-of-a-key-in-nested-dictionaries-and-lists

def gen_dict_extract(key, var):
    """Extracts all occurrences of a keyword in a nested dictionary that may include lists of dictionaries

    :param var: the dictionary to be searched
    :param key: the key being searched for
    :return: a generator yielding all values related to the key
    """
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


if __name__ == '__main__':
    folder_name = "../weather/data/"
    file_obs = 'ice_observations.json'
    filepath = folder_name + file_obs


    def load_json(file_name):
        with open(file_name) as infile:
            return json.load(infile)


    observations = load_json(filepath)

    print(list(gen_dict_extract('main', observations[0])))  # list, um mehrfache Ergebnisse anzuzeigen
    print(next(gen_dict_extract('pressure', observations[0])))
    print(list(gen_dict_extract('id', observations[0])))
    pprint.pprint(observations[0])
