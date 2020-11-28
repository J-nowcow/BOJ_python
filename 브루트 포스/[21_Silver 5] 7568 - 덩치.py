N = int(input())
lst = [input().split() for _ in range(N)]
a = [1 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            a[i] += 1

print(" ".join(map(str,a)))
