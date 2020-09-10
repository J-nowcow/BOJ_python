N = int(input())
cost = [list(map(int,input().split())) for _ in range(N)]

def find(visited,now):

    # 남아있는 경로를 이미 방문한 적이 있으면 바로 리턴해준다.
    if dp[visited][now]: return dp[visited][now]

    # 모든 방을 방문한 경우라면 0번으로 돌아갈 수 있을 때 그 값을, 아니면 매우 큰 더미 값을 리턴한다.
    if visited == (1<<N) - 1:
        return cost[now][0] if cost[now][0] > 0 else 10**9
    
    tmp = 10**8
    # 0번 방을 제외하고, 다음에 갈 방을 골라준다.
    for i in range(1,N):
        # (visited >> i) % 2 == 0 이어야 아직 방문하지 않은 방이다.
        # cost[now][i] == 0이면 길이 없는 경우니까 패스한다.
        if (not (visited >> i) % 2) and cost[now][i]:
            tmp = min(tmp, find(visited | (1<<i), i) + cost[now][i])

    dp[visited][now] = tmp
    return tmp
dp = [[0]*N for _ in range(1<<N)]

print(find(1,0))
