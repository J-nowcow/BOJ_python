import sys
input = sys.stdin.readline

N = int(input())
a = [input().rstrip() for _ in range(N)]
heart = -1
for i in range(N):
    for j in range(N):
        if a[i][j] == "*":
            heart = (i+1,j)
            break
    if heart != -1:
        break

ans = [0,0,0,0,0]
for i in range(heart[1]-1,-1,-1):
    if a[heart[0]][i] == "*":
        ans[0] += 1
    else: break
    
for i in range(heart[1]+1,N):
    if a[heart[0]][i] == "*":
        ans[1] += 1
    else: break
    
for i in range(heart[0]+1,N):
    if a[i][heart[1]] == "*":
        ans[2] += 1
    else:
        tmp = i
        break

for i in range(tmp,N):
    if a[i][heart[1]-1] == "*":
        ans[3] += 1
    if a[i][heart[1]+1] == "*":
        ans[4] += 1

print(heart[0]+1, heart[1]+1)
for i in ans:
    print(i, end=" ")
