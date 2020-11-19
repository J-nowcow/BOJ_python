"""
(0,9),(1,8),(2,7),(3,6),(4,5) 한 쌍으로 묶고 각각 a,b,c,d,e로 할당
한 자리 넘어갈 때마다
a = b
b = a+c, c = b+d, d = c+e, e = d + e
시작할 때 a = 1, b,c,d,e = 2 (0으로 시작은 불가능하므로)
"""
a = 1
b = c = d = e = 2
for i in range(int(input())-1):
    a, b, c, d, e = b, a+c, b+d, c+e, d+e
    
print((a+b+c+d+e)%10**9)
