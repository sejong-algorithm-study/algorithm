def solution(record):
    answer = []

    user = {}
    for r in record:
        comment = r.split()
        if len(comment) == 3:
            id = comment[1]
            user[id] = comment[2]

    for r in record:
        comment = r.split()
        result = user[comment[1]]
        if comment[0] == 'Enter':
            result += '님이 들어왔습니다.'
        elif comment[0] == 'Leave':
            result += '님이 나갔습니다.'
        elif comment[0] == 'Change':
            continue
        answer.append(result)

    return answer