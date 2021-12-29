string = list(input())

is_same = True
for i in range(len(string) - 1):
    if string[i] != string[i + 1]:
        is_same = False
        break

if is_same:
    print(-1)
else:
    is_palindrome = True
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            is_palindrome = False
            break

    if is_palindrome:
        print(len(string) - 1)
    else:
        print(len(string))
