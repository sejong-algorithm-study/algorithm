import sys
n = int(sys.stdin.readline())
answer= {}
arr= list(map(int,sys.stdin.readline().split()))
for i in range(n):
    answer[arr[i]]=1
m = int(sys.stdin.readline())
guess = list(map(int,sys.stdin.readline().split()))
for i in guess:
    if i in answer:
        print(1, end=" ")
    else:
        print(0,end=" ")

