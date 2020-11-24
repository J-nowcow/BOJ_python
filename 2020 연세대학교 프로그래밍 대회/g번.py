from collections import deque

N,M = map(int,input().split())
m = [input() for _ in range(N)]

for i in range(N):
    if "@" in m[i]:
        start = [i,m[i].index("@")]
        break

ans = [] + [start]
check = [[-1]*M for _ in range(N)]
check[start[0]][start[1]] = 0

q = deque([start])
key = {}
for i in range(97,97+26):
    key[chr(i)] = -1  

d = ((0,1),(0,-1),(-1,0),(1,0))
success = False
while not success:
    ta, tb = q.popleft()
    c = 0
    for i in d:
        a = ta + i[0] ; b = tb + i[1]
        if 0 <= a < N and 0 <= b < M:
            if check[a][b] == -1:
                if m[a][b] == "!":
                    success = True
                    ans.append([a,b])
                    break
                
                elif "A" <= m[a][b] <= "Z" and key[m[a][b].lower()] == 1:
                    check[a][b] = 0
                    ans.append([a,b])
                    q.append([a,b])
                    c = 1
                elif "a" <= m[a][b] <= "z":
                    check[a][b] = 0
                    ans.append([a,b])
                    key[m[a][b]] = 1
                    q.append([a,b])
                    c = 1
                elif m[a][b] == "*":
                    check[a][b] = 0
                    ans.append([a,b])
                    q.append([a,b])
                    c = 1
    for i in d:
        a = ta + i[0] ; b = tb + i[1]
        if 0 <= a < N and 0 <= b < M:
            if "A" <= m[a][b] <= "Z" and key[m[a][b].lower()] == -1:
                c = 0
    if c == 0:
        q.append([ta,tb])

print(len(ans))
for i in ans:
    print(i[0]+1, i[1]+1)
