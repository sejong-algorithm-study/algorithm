import sys
n,l=map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

totalcnt = 0

for i in range(n):
    now = arr[i][0]
    cnt = 1
    j=1
    samefloor = 1
    while j<n:
        if now==arr[i][j]: #층이 같으면 쭉 가기
            cnt+=1
            j+=1
            samefloor+=1
            continue
        elif now+1<arr[i][j] or now-1 >arr[i][j]: # 2층 이상 차이나면 끝내기
            break
        elif now+1 == arr[i][j]: # 층이 하나 높을 경우
            if samefloor>=l:#지금까지 층이 같은게 l보다 크거나 같으면 경사로 놓을 수 있음
                samefloor=1
                cnt+=1
                now = arr[i][j]
                j+=1
            else:
                break
        elif now-1 == arr[i][j]:
            tmp = 0
            for k in range(l):
                if j+k<n and arr[i][j+k] ==arr[i][j]:
                    tmp+=1
                    continue
                else:
                    tmp = -1
                    break
            if tmp ==-1:
                break
            if tmp == l:
                now = arr[i][j]
                cnt+=l
                j+=l
                samefloor = 0
                continue
    if cnt == n:
        totalcnt+=1

for i in range(n):
    now = arr[0][i]
    cnt = 1
    j=1
    samefloor = 1
    while j<n:
        if now==arr[j][i]: #층이 같으면 쭉 가기
            cnt+=1
            j+=1
            samefloor+=1
            continue
        elif now+1<arr[j][i] or now-1 >arr[j][i]: # 2층 이상 차이나면 끝내기
            break
        elif now+1 == arr[j][i]: # 층이 하나 높을 경우
            if samefloor>=l:#지금까지 층이 같은게 l보다 크거나 같으면 경사로 놓을 수 있음
                samefloor=1
                cnt+=1
                now = arr[j][i]
                j+=1
            else:
                break
        elif now-1 == arr[j][i]:
            tmp = 0
            for k in range(l):
                if j+k<n and arr[j+k][i] ==arr[j][i]:
                    tmp+=1
                    continue
                else:
                    tmp = -1
                    break
            if tmp ==-1:
                break
            if tmp == l:
                now = arr[j][i]
                cnt += l
                j += l
                samefloor = 0
                continue
    if cnt == n:
        totalcnt+=1


print(totalcnt)