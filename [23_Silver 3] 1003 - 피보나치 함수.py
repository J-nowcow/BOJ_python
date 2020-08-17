"""
0: 1 0으로 시작하는 피보나치 수열
1: 0 1로 시작하는 피보나치 수열
-> a,b = 1,0으로 시작하고 a,b = b,a+b로 두면 됨
"""
for _ in range(int(input())):
    n = int(input())
    a,b = 1,0
    for i in range(n):
        a,b = b,a+b
    print(a,b)
