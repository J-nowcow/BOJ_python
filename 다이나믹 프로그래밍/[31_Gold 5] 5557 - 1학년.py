"""
0~20까지 담을 수 있는 dp 만들기
dp[k][n] = k번 째 숫자까지 더한 값이 n인 경우의 수
+ - 각각에 대해 계산해서 dp 값 업데이트
"""
n = int(input()) - 1
*a, = map(int,input().split())

dp = [[0 for i in range(21)] for j in range(n)]
dp[0][a[0]] = 1

for i in range(1,n):
    for j in range(21):
        if 0 <= j+a[i] < 21: dp[i][j+a[i]] += dp[i-1][j]
        if 0 <= j-a[i] < 21: dp[i][j-a[i]] += dp[i-1][j]

print(dp[-1][a[-1]])
