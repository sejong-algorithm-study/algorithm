def solution(brown, yellow):
    if brown == yellow:
        for i in range(1, yellow+ 1):
            for j in range(i, yellow + 1):
                y = 2*(j + 2) + 2*i + i*j
                if yellow == y:
                    print(i,j)
                    return  (j + 2, 2*(i + 2))
    elif brown > yellow:
        for i in range(1, yellow+ 1):
            for j in range(i, yellow + 1):
                y = i * j
                b = 2*(i)+ 2*(j+2)
                print(y, b)
                if y == yellow and b == brown: 
                    return (j + 2, i + 2)
                    
    else:
        for i in range(1, brown+ 1):
            for j in range(i, brown + 1):
                y = i * j
                b = 2*(i) + 2*(j+2)
                if y == yellow and b == brown: 
                    return  (j + 2, i + 2)