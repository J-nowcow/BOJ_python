import sys
input = sys.stdin.readline

n,m,s = map(int,input().split())
time = [(0,0)]
for i in range(n):
    time.append(tuple(map(int,input().split())))

time.sort()

for i in range(n):
    if time[i+1][0] - (time[i][0]+time[i][1]) >= m:
        print(time[i][0]+time[i][1])
        break
else:
    if s - (time[-1][0] + time[-1][1]) >= m:
        print(time[-1][0] + time[-1][1])
    else:
        print(-1)
