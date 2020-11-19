"""
문자열의 S~E 번 째 글자가 팰린드롬인가?
N = 2000이므로 2000C2 = 2*10^6 개의 케이스 전부 미리 계산해둘 수 있음
M = 10^6이기 때문에 이쪽을 건드리는 것보다 계산해놓고 하나씩 바로바로 출력하기

dp[x][y]: x~y (x,y포함) 가 펠린드롬이면 1, 아니면 0
dp[x][y]: dp[x-1][y-1] == 1 이고 num[x] == num[y] 이면 1, 하나라도 아니면 0

초기값: y = x+1 일 때는 num[x] == num[y] 일 때 1
y = x 일 때는 항상 1

for문은 하나는 고를 숫자의 개수로, 하나는 시작 지점으로 돌려주
"""
import sys
input = sys.stdin.readline
N = int(input())
num = input().split()
dp = [[1] * N for _ in range(N)]

for a in range(N):
    for S in range(N - a):
        E = S + a
        if a == 0: continue
        elif a == 1:
            if num[S] != num[E]: dp[S][E] = 0
        else:
            if dp[S+1][E-1] == 0 or num[S] != num[E]: dp[S][E] = 0

M = int(input())
for i in range(M):
    S,E = map(int,input().split())
    print(dp[S-1][E-1])
