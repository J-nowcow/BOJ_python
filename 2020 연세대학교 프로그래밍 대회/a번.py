import sys
input = sys.stdin.readline

N = int(input())
m = ["zzzzzzzz",-1]
for i in range(N):
    a,b = input().split()
    if int(b) > m[1]:
        m[1] = int(b)
        m[0] = a
    elif int(b) == m[1]:
        m[0] = min(a,m[0])

print(m[0])
