# 효율적인 코드
def solution(brown, yellow):
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            j = yellow // i
            if (i + j) * 2 + 4 == brown:
                return [j + 2, i + 2]

# list comprehension을 사용했지만, 이렇게 작성하게 될 줄은 몰랐어,,,
def solution(brown, yellow):
	return [[yellow // i + 2, i + 2] for i in range(1, yellow + 1) if yellow % i == 0 and (i + yellow // i) * 2 + 4 == brown][0]