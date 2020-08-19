"""
Combination 계산하기: nCk = n!/k!(n-k)! = (n)(n-1)...(n-k+1)/(1)(2)...(k)
1부터 나눠주면 모든 중간 계산값이 정수로 나옴을 증명할 수 있음.
"""
n,k = map(int,input().split())
a = 1
for i in range(k):
    a *= (n-i)//(i+1)
print(a%10007)
