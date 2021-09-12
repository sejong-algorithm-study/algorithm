import sys

def DFS( n, line, o1, o2,i):
    if o1>o2:
        temp = o1
        o1=o2
        o2=temp

    if i==n-1:
        return min(abs(line[i]-o1),abs(line[i]-o2))

    d1=DFS(n,line,line[i],o2,i+1)
    d2=DFS(n,line,o1,line[i],i+1)
    return min(abs(o1-line[i])+d1,abs(o2-line[i])+d2)

input = sys.stdin.readline
closetlength = int(sys.stdin.readline())
o1, o2 = map(int, input().split())
o1 -= 1
o2 -= 1
n = int(sys.stdin.readline())
line = [int(sys.stdin.readline()) - 1 for i in range(n)]


print(DFS( n, line, o1, o2,0))
