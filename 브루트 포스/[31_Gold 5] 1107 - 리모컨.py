"""
#1. |이동할 채널 - 100|
#2. 채널보다 작은 수 중 가장 큰 수
#3. 채널보다 큰 수 중 가장 작은 수
"""

N = int(input())
M = int(input())
if not M:
    print(min(abs(100 - N), len(str(N))))
else:
    b = input().split()

    # case 1.
    ans = abs(100 - N)

    # case 2.
    num = N
    while num < N + ans:
        for i in str(num):
            if i in b:
                break
        else:
            ans = min(ans, len(str(num)) + (num - N))
            break
        num += 1

    # case 3.
    num = N
    while num >= max(N - ans,0):
        for i in str(num):
            if i in b:
                break
        else:
            ans = min(ans, len(str(num)) + (N - num))
            break
        num -= 1

    print(ans)
