"""
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

Example:
    list1 = [1, 2, 3, 2, 1]
    list2 = [3, 1, 2, 1, 3]
    check_same_frequency(list1, list2)

Output:
    False
"""


def check_same_frequency(list1, list2):
    def count_elements(lst):
        counted = {}
        for el in lst:
            counted[el] = counted.get(el, 0) + 1
        return counted

    return count_elements(list1) == count_elements(list2)


list_1 = [1, 2, 3, 2, 1]
list_2 = [3, 1, 2, 1, 3]
result = check_same_frequency(list_1, list_2)
print(result)
