import math


def solution(fees, records):
    answer = {}
    cars = {}
    dt, df, pt, pf = fees

    for record in records:
        time, car, state = record.split(' ')
        h, m = map(int, time.split(':'))
        minutes = h * 60 + m

        if state == 'IN':
            cars[car] = minutes
        else:
            parking_time = minutes - cars[car]
            del cars[car]

            # 요금 계산
            total_fee = df
            if parking_time > dt:
                total_fee += math.ceil((parking_time - dt) / pt) * pf

            if car in answer:
                answer[car] += total_fee
            else:
                answer[car] = total_fee

    # 아직 출차되지 않은 경우(출차 기록이 없는 경우)
    if cars:
        for car in cars.keys():
            parking_time = 23 * 60 + 59 - cars[car]

            # 요금 계산
            total_fee = df
            if parking_time > dt:
                total_fee += math.ceil((parking_time - dt) / pt) * pf

            if car in answer:
                answer[car] += total_fee
            else:
                answer[car] = total_fee

    answer = list(answer.items())
    answer.sort()

    return [fee for car, fee in answer]


print(solution([120, 0, 60, 591],
               ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
