def count_word_frequency(words):
    info_dict = {}
    for word in words:
        if word not in info_dict.keys():
            info_dict.setdefault(word, 1)
        else:
            info_dict[word] += 1
    return info_dict


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
result = count_word_frequency(words)
print(result)
