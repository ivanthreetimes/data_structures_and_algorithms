"""
Define a function which takes two dictionaries as parameters
and merge them and sum the values of common keys.

Example:
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    merge_dicts(dict1, dict2)

Output:
    {'a': 1, 'b': 5, 'c': 7, 'd': 5}
"""


def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for k, v in dict2.items():
        result[k] = result.get(k, 0) + v
    return result


dict_1 = {'a': 1, 'b': 2, 'c': 3}
dict_2 = {'b': 3, 'c': 4, 'd': 5}
result = merge_dicts(dict_1, dict_2)
print(result)
