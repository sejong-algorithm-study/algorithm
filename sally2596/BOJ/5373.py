import sys
import copy

n = int(sys.stdin.readline())
char = ['w', 'g', 'r', 'b', 'o', 'y']
origincube = []
cube=[]
for j in range(6):
    origincube.append([[char[j] for k in range(3)] for i in range(3)])

def move(up, left, top, right, down, clockwise):
    if clockwise:  # 시계 방향이면
        t1, t2, t3 = cube[up[0]][up[1][0]][up[1][1]], cube[up[0]][up[2][0]][up[2][1]], cube[up[0]][up[3][0]][up[3][1]]
        cube[up[0]][up[1][0]][up[1][1]], cube[up[0]][up[2][0]][up[2][1]], cube[up[0]][up[3][0]][up[3][1]] = \
        cube[left[0]][left[3][0]][left[3][1]], cube[left[0]][left[2][0]][left[2][1]], cube[left[0]][left[1][0]][left[1][1]]
        cube[left[0]][left[1][0]][left[1][1]], cube[left[0]][left[2][0]][left[2][1]], cube[left[0]][left[3][0]][
            left[3][1]] = cube[down[0]][down[1][0]][down[1][1]], cube[down[0]][down[2][0]][down[2][1]], \
                          cube[down[0]][down[3][0]][down[3][1]]
        cube[down[0]][down[1][0]][down[1][1]], cube[down[0]][down[2][0]][down[2][1]], cube[down[0]][down[3][0]][
            down[3][1]] = cube[right[0]][right[3][0]][right[3][1]], cube[right[0]][right[2][0]][right[2][1]], \
                          cube[right[0]][right[1][0]][right[1][1]]
        cube[right[0]][right[1][0]][right[1][1]], cube[right[0]][right[2][0]][right[2][1]], cube[right[0]][right[3][0]][
            right[3][1]] = t1, t2, t3

        temparr = copy.deepcopy(cube[top])
        for j in range(3):
            for k in range(3):
                cube[top][k][2-j] = temparr[j][k]

    else:
        t1, t2, t3 = cube[up[0]][up[1][0]][up[1][1]], cube[up[0]][up[2][0]][up[2][1]], cube[up[0]][up[3][0]][up[3][1]]
        cube[up[0]][up[1][0]][up[1][1]], cube[up[0]][up[2][0]][up[2][1]], cube[up[0]][up[3][0]][up[3][1]] = \
        cube[right[0]][right[1][0]][right[1][1]], cube[right[0]][right[2][0]][right[2][1]], cube[right[0]][right[3][0]][
            right[3][1]]
        cube[right[0]][right[1][0]][right[1][1]], cube[right[0]][right[2][0]][right[2][1]], cube[right[0]][right[3][0]][
            right[3][1]] = cube[down[0]][down[3][0]][down[3][1]], cube[down[0]][down[2][0]][down[2][1]], \
                           cube[down[0]][down[1][0]][down[1][1]]
        cube[down[0]][down[1][0]][down[1][1]], cube[down[0]][down[2][0]][down[2][1]], cube[down[0]][down[3][0]][
            down[3][1]] = cube[left[0]][left[1][0]][left[1][1]], cube[left[0]][left[2][0]][left[2][1]], \
                          cube[left[0]][left[3][0]][left[3][1]]
        cube[left[0]][left[1][0]][left[1][1]], cube[left[0]][left[2][0]][left[2][1]], cube[left[0]][left[3][0]][
            left[3][1]] = t3, t2, t1

        temparr = copy.deepcopy(cube[top])
        for j in range(3):
            for k in range(3):
                cube[top][2-k][j] = temparr[j][k]


def turn():
    for j in arr:
        if j == 'U+':
            move([4, [0, 2], [0, 1], [0, 0]], [1, [0, 0], [0, 1], [0, 2]], 0, [3, [0, 2], [0, 1], [0, 0]],
                 [2, [0, 0], [0, 1], [0, 2]], True)
        elif j == 'U-':
            move([4, [0, 2], [0, 1], [0, 0]], [1, [0, 0], [0, 1], [0, 2]], 0, [3, [0, 2], [0, 1], [0, 0]],
                 [2, [0, 0], [0, 1], [0, 2]], False)
        elif j == 'D+':
            move([2, [2, 0], [2, 1], [2, 2]], [1, [2, 2], [2, 1], [2, 0]], 5, [3, [2, 0], [2, 1], [2, 2]],
                 [4, [2, 2], [2, 1], [2, 0]], True)
        elif j == 'D-':
            move([2, [2, 0], [2, 1], [2, 2]], [1, [2, 2], [2, 1], [2, 0]], 5, [3, [2, 0], [2, 1], [2, 2]],
                 [4, [2, 2], [2, 1], [2, 0]], False)
        elif j == 'F+':
            move([0, [2, 0], [2, 1], [2, 2]], [1, [0, 2], [1, 2], [2, 2]], 2, [3, [0, 0], [1, 0], [2, 0]],
                 [5, [0, 0], [0, 1], [0, 2]], True)
        elif j == 'F-':
            move([0, [2, 0], [2, 1], [2, 2]], [1, [0, 2], [1, 2], [2, 2]], 2, [3, [0, 0], [1, 0], [2, 0]],
                 [5, [0, 0], [0, 1], [0, 2]], False)
        elif j == 'B+':
            move([0, [0, 2], [0, 1], [0, 0]], [3, [0, 2], [1, 2], [2, 2]], 4, [1, [0, 0], [1, 0], [2, 0]],
                 [5, [2, 2], [2, 1], [2, 0]], True)
        elif j == 'B-':
            move([0, [0, 2], [0, 1], [0, 0]], [3, [0, 2], [1, 2], [2, 2]], 4, [1, [0, 0], [1, 0], [2, 0]],
                 [5, [2, 2], [2, 1], [2, 0]], False)
        elif j == 'L+':
            move([0, [0, 0], [1, 0], [2, 0]], [4, [0, 2], [1, 2], [2, 2]], 1, [2, [0, 0], [1, 0], [2, 0]],
                 [5, [2, 0], [1, 0], [0, 0]], True)
        elif j == 'L-':
            move([0, [0, 0], [1, 0], [2, 0]], [4, [0, 2], [1, 2], [2, 2]], 1, [2, [0, 0], [1, 0], [2, 0]],
                 [5, [2, 0], [1, 0], [0, 0]], False)
        elif j == 'R+':
            move([0, [2, 2], [1, 2], [0, 2]], [2, [0, 2], [1, 2], [2, 2]], 3, [4, [0, 0], [1, 0], [2, 0]],
                 [5, [0, 2], [1, 2], [2, 2]], True)
        elif j == 'R-':
            move([0, [2, 2], [1, 2], [0, 2]], [2, [0, 2], [1, 2], [2, 2]], 3, [4, [0, 0], [1, 0], [2, 0]],
                 [5, [0, 2], [1, 2], [2, 2]], False)


for i in range(n):
    num = int(sys.stdin.readline())
    arr = list(map(str, sys.stdin.readline().rstrip().split()))
    cube = copy.deepcopy(origincube)
    turn()
    for j in range(3):
        for k in range(3):
            print(cube[0][j][k],end="")
        print()
