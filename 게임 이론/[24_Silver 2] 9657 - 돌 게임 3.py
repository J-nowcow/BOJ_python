"""
dp로 주기성 찾은 다음에, 그 주기에 맞게 출력해주기
dp[n]: dp[n-1], dp[n-3], dp[n-4] 중 0이 있으면 1 아니면 0
1: 상근이가 이김, 0: 창영이가 이김
"""

"""
dp = [0]*30
dp[1] = 1; dp[2] = 0; dp[3] = 1; dp[4] = 1

for i in range(5,30):
    if 0 in (dp[i-1], dp[i-3], dp[i-4]): dp[i] = 1

print(dp[1:])
"""
# 1 0 1 1 1 1 0 반복 -> mod 7에 대해 0,2면 CY, 아니면 SK
print(["SK","CY"][int(input()) % 7 in (0,2)])
# print("SCKY"[int(input())%7 in(0,2)::2])
