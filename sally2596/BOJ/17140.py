import sys
from collections import Counter

r,c,k = map(int,sys.stdin.readline().split())
arr= [[0 for _ in range(100)] for i in range(100)]
for i in range(3):
    arr[i][0],arr[i][1],arr[i][2] = map(int,sys.stdin.readline().split())
cnt = 0

row =3
column=3

# len(arr) 이 row 개수 :행
# len(arr[0])이 column 개수 : 열

def R():
    maxrow=0
    for i in range(row):
        temp=[]
        counter = Counter(arr[i])
        del(counter[0])
        counter = sorted(counter.items(), key = lambda x :[x[1], x[0]])
        for (a,b) in counter:
            temp.append(a)
            temp.append(b)
        maxrow = max(maxrow,len(temp))
        if len(temp)<100:
            temp+=[0]*(100-len(temp))
        arr[i] = temp[:100]
    return maxrow
def C():
    maxcolumn = 0
    length = 0
    for i in range(column):
        temp = []
        counter = Counter(list(zip(*arr))[i])
        del (counter[0])
        counter = sorted(counter.items(), key=lambda x: [x[1], x[0]])
        for (a, b) in counter:
            temp.append(a)
            temp.append(b)
        length=len(temp)
        maxcolumn = max(maxcolumn, len(temp))
        if len(temp) < 100:
            temp += [0] * (100 - len(temp))
        temp = temp[:100]
        for j in range(100):
            arr[j][i] = temp[j]
    return maxcolumn

while  cnt<=100 and arr[r-1][c-1]!=k:
    if row>=column:
        column = R()
    else:
        row = C()
    cnt+=1
if cnt<=100:
    print(cnt)
else:
    print(-1)