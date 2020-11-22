from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
d = {}
for i in range(N):
    d[i+1] = []
for i in range(M):
    a,b,c = map(int, input().split())
    d[a].append((b,c))
    d[b].append((a,c))

cost = [[-1,-1] for _ in range(N+1)]
cost[1][0] = 0
q = deque([1])
while q:
    a = q.popleft()
    for i in d[a]:
        if cost[a][0] != -1 and ((cost[i[0]][(cost[a][0] + i[1])%2] == -1) or cost[a][0] + i[1] < cost[i[0]][(cost[a][0] + i[1])%2]):
            cost[i[0]][(cost[a][0] + i[1]) % 2] = cost[a][0] + i[1]
            q.append(i[0])
        if cost[a][1] != -1 and ((cost[i[0]][(cost[a][1] + i[1])%2] == -1) or cost[a][1] + i[1] < cost[i[0]][(cost[a][1] + i[1])%2]):
            cost[i[0]][(cost[a][1] + i[1]) % 2] = cost[a][1] + i[1]
            q.append(i[0])
for i,j in cost[1:]:
    print(j,i)
