import sys

n = int(sys.stdin.readline())
maxarr = [0] * 3
minarr = [0] * 3

for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())

    ta,tb,tc = maxarr[0],maxarr[1],maxarr[2]
    maxarr[0] =a+max(ta,tb)
    maxarr[1] = b + max(ta, tb, tc)
    maxarr[2] = c + max(tb, tc)

    ta, tb, tc =minarr[0], minarr[1], minarr[2]
    minarr[0] =a+min(ta,tb)
    minarr[1] = b+min(ta,tb,tc)
    minarr[2] =c+min(tb,tc)

print(max(maxarr), min(minarr))
