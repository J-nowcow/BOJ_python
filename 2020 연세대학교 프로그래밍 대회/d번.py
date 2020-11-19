import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))

point = [0]
check = 0
for i in range(N-1):
    if a[i] > a[i+1]:
        if check != 2:
            point.append(i+1)
        check = 2
    elif a[i] < a[i+1]:
        if check != 1:
            point.append(i+1)
        check = 1
if len(point) > 10:
    print(-1)
else:
    for pos in point:
        tmp = a[pos:] + a[:pos]
        check = 0
        for i in range(N-1):
            if tmp[i] > tmp[i+1]:
                if check == 1:
                    check = -1; break
                check = 2
            elif tmp[i] < tmp[i+1]:
                if check == 2:
                    check = -1; break
                check = 1
        if check != -1:
            print(pos)
            break
    else:
        print(-1)
