# N의 생성자는 N-60 ~ N 사이에만 존재할 수 있음

N = int(input())
for i in range(max(0,N-60),N+1):
    tmp = i
    for j in str(tmp):
        tmp += int(j)
    if tmp == N:
        print(i)
        break
else:
    print(0)
