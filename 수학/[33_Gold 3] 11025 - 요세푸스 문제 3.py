n,k = map(int,input().split())
f = 0
for i in range(2,n+1):
    f = (f + k) % i
print(f+1)
