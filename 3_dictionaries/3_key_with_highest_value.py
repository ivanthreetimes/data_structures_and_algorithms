"""
Define a function which takes a dictionary as a parameter
and returns the key with the highest value in a dictionary.

Example:
    my_dict = {'a': 5, 'b': 9, 'c': 2}
    max_value_key(my_dict)

Output:
    b
"""


def max_value_key(my_dict):
    highest_value_key = ['key_name', float('-inf')]
    for k, v in my_dict.items():
        if v > highest_value_key[1]:
            highest_value_key = [k, v]
    return highest_value_key[0]


mydict = {'a': 5, 'b': 9, 'c': 2}
result = max_value_key(mydict)
print(result)
