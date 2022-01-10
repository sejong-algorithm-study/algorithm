import math
from collections import Counter


def valid_word(word):
    return 'A' <= word[0] <= 'Z' and 'A' <= word[1] <= 'Z'


def solution(str1, str2):
    answer = 0

    set1 = []
    set2 = []

    str1 = str1.upper()
    str2 = str2.upper()

    for i in range(len(str1) - 1):
        tmp = str1[i:i + 2]
        if (valid_word(tmp)):
            set1.append(tmp)

    for i in range(len(str2) - 1):
        tmp = str2[i:i + 2]
        if (valid_word(tmp)):
            set2.append(tmp)

    dict1 = dict(Counter(set1))
    dict2 = dict(Counter(set2))

    elements = set(list(dict1.keys()) + list(dict2.keys()))

    if len(elements) == 0:
        answer = 1
    else:
        union = 0
        intersect = 0

        for element in elements:
            is_in_dict1 = element in dict1
            is_in_dict2 = element in dict2

            if is_in_dict1 and is_in_dict2:
                union += max(dict1[element], dict2[element])
                intersect += min(dict1[element], dict2[element])
            elif is_in_dict1:
                union += dict1[element]
            else:
                union += dict2[element]

        answer = intersect / union if intersect > 0 else 0

    return math.floor(answer * 65536)