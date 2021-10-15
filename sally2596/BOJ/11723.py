import sys

que = dict({1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0})
n = int(sys.stdin.readline())

for i in range(n):
    type = sys.stdin.readline().rstrip().split()
    if type[0] == "add":
        if que[int(type[1])] == 0:
            que[int(type[1])] = 1
    elif type[0] == "remove":
        que[int(type[1])] = 0
    elif type[0] == "check":
        if que[int(type[1])] == 1:
            print("1")
        else:
            print("0")
    elif type[0] == "toggle":
        que[int(type[1])] = 0 if que[int(type[1])] == 1 else 1
    elif type[0] == "all":
        que.update({1:1,2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1,17:1,18:1,19:1,20:1})
    elif type[0]=="empty":
        que.update({1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0})
