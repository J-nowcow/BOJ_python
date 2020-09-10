N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]

def find(visited,now):
    if dp[visited][now]: return dp[visited][now]
    if visited == (1<<N) - 1:
        return ((cost[0][0] - cost[now][0])**2 + (cost[0][1] - cost[now][1])**2)**0.5

    tmp = 10**8
    for i in range(1,N):
        if not (visited >> i) % 2:
            tmp = min(tmp, find(visited | (1<<i), i) + ((cost[i][0]-cost[now][0])**2 + (cost[i][1]-cost[now][1])**2)**0.5)

    dp[visited][now] = tmp
    return tmp
dp = [[0]*N for _ in range(1<<N)]

print(find(1,0))
