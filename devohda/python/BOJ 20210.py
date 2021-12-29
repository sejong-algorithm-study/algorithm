from functools import cmp_to_key


def is_alphabet(char):
    if 'A' <= char <= 'Z':
        return (ord(char) - ord('A')) * 2 + 1
    elif 'a' <= char <= 'z':
        return (ord(char) - ord('a')) * 2 + 2
    else:
        return 0


N = int(input())
strings = []
for _ in range(N):
    strings.append(input())


def cmp_items(str1, str2):
    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(str1) and ptr2 < len(str2):
        alpha1 = is_alphabet(str1[ptr1])
        alpha2 = is_alphabet(str2[ptr2])
        if alpha1 and alpha2:
            if alpha1 < alpha2:
                return -1
            elif alpha2 < alpha1:
                return 1
        elif alpha1:
            while ptr2 < len(str2) and not is_alphabet(str2[ptr2]):
                ptr2 += 1
            ptr2 -= 1

            return 1
        elif alpha2:
            while ptr1 < len(str1) and not is_alphabet(str1[ptr1]):
                ptr1 += 1
            ptr1 -= 1

            return -1
        else:
            num1 = 0
            num2 = 0

            cnt1 = 0
            cnt2 = 0

            while ptr1 < len(str1) and not is_alphabet(str1[ptr1]):
                num1 *= 10
                num1 += int(str1[ptr1])
                ptr1 += 1
                cnt1 += 1
            ptr1 -= 1

            while ptr2 < len(str2) and not is_alphabet(str2[ptr2]):
                num2 *= 10
                num2 += int(str2[ptr2])
                ptr2 += 1
                cnt2 += 1
            ptr2 -= 1

            if num1 < num2:
                return -1
            elif num2 < num1:
                return 1
            else:
                if cnt1 < cnt2:
                    return -1
                elif cnt2 < cnt1:
                    return 1

        ptr1 += 1
        ptr2 += 1

    if len(str1) > len(str2):
        return 1
    elif len(str1) < len(str2):
        return -1
    else:
        return 0


strings = sorted(strings, key=cmp_to_key(cmp_items))

for string in strings:
    print(string)
