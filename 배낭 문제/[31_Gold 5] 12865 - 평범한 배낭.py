"""
평범한 0-1 냅색 문제
dp[100][100000]짜리 만들기
dp[i][j]: i번째까지 가치의 최댓값

dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
만약 i보다 weight[i]가 더 크다면 dp[i][j] = dp[i-1][j]
"""
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
weight = [0]
value = [0]

for i in range(N):
    a,b = map(int, input().split())
    weight += [a]
    value += [b]

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= weight[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
