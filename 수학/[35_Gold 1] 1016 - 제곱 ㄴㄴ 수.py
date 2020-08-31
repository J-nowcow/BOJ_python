"""
1557번 문제를 해결했다면 동일한 방법으로 더 빠른 시간 안에 해결할 수 있다.
하지만 그 문제가 더 난이도가 높으므로 다른 방법을 사용해보자.

1. sqrt(max) 이하의 소수 구하기 (에라토스테네스의 체)
2. [min,max] 에 대해 각각의 소수에 대해 소수 제곱으로 나누어지는지 계산하기

max의 범위 10^12이므로 sqrt(max)는 10^6
소수의 개수는 대충 x/lnx에 비례하므로 약 10^6/6개
집합으로 만든 다음 빼주기

근데 소수 찾는게 너무 시간 많이 걸려서 바로 제곱수 빼는게 더 빠름
"""

start, end = map(int,input().split())

ans = set(range(start,end+1))

for i in range(2,int(end**0.5)+1):
    i *= i
    ans -= set(range((start//i)*i,(end//i + 1)*i,i))

print(len(ans))
