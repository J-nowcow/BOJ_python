"""
총합이 n이 되게 하는 가격의 최댓값을 구하는 문제
dp[k] = max(p[k],dp[k-1]+dp[0], dp[k-2]+dp[1], ..., dp[k//2+1]+dp[k//2])
"""

n = int(input())
*p, = map(int, input().split())

dp = [0] * n
for i in range(n):
    tmp = p[i]
    for j in range(i//2+1):
        tmp = max(tmp, dp[j] + dp[i-j-1])
    dp[i] = tmp

print(dp[-1])
