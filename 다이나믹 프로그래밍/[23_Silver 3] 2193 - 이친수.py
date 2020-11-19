"""
a: 마지막 자릿수가 1, b: 0
k번 째 자리 1: k-1번 째 자리 0
k번 째 자리 0: k-1자리 수의 개수
-> a, b = b, a+b
"""
a, b = 1, 0
for i in range(int(input())-1):
    a, b = b, a+b
print(a+b)
