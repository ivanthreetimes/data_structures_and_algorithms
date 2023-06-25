"""
Define a function to count the frequency of
words in a given list of words.

Example:
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
    count_word_frequency(words)

Output:
     {'apple': 3, 'orange': 2, 'banana': 1}
"""


def count_word_frequency(words):
    info_dict = {}
    for word in words:
        info_dict[word] = info_dict.get(word, 0) + 1
    return info_dict


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
result = count_word_frequency(words)
print(result)
