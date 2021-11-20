import sys

n = int(sys.stdin.readline())
a = []
b = []
c = []
d = []
ab=[]
cd={}
for i in range(n):
    n1, n2, n3, n4 = map(int, sys.stdin.readline().split())
    a.append(n1)
    b.append(n2)
    c.append(n3)
    d.append(n4)

k=0
for i in range(n):
    for j in range(n):
        ab.append(a[i]+b[j])
        if c[i]+d[j] in cd:
            cd[c[i]+d[j]]+=1
        else:
            cd[c[i]+d[j]]=1
        k+=1

cnt=0

for i in ab:
    if -i in cd:
        cnt+=cd[-i]

print(cnt)