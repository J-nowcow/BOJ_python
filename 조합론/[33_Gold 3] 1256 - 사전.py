"""
a가 n개, z가 m개
-> a로 시작하는 경우 (n+m-1)Cm, z로 시작하는 경우 (n+m-1)Cn
첫칸부터 하나씩 줄여나가면서 계산하기
(n+m-1)Cm = (n+m-1)!/m!(n-1)! = (n+m-1)(n+m-2)...(n)/(1)(2)...(m)
"""

n,m,k = map(int,input().split())

ans = ""
# -1 예외처리
tmp = 1
for i in range(1,m+1):
    tmp *= (n+i)
    tmp //= (i)

if tmp < k: print(-1)
else:
    ans = ""
    s = n+m
    for _ in range(s):
        tmp = 1
        for i in range(1,m+1):
            tmp *= (n+i-1)
            tmp //= (i)
        # tmp > k면 a, 아니면 z
        if tmp >= k:
            ans += "a"
            n -= 1
        else:
            ans += "z"
            m -= 1
            k -= tmp

        if n == 0: print(ans + "z"*m); break
        if m == 0: print(ans + "a"*n); break
