N,M = map(int, input().split())
m = [input() for _ in range(N)]

ans = N*M
for x in range(N-7):
    for y in range(M-7):
        for a in range(2):
            tmp = 0
            for i in range(x,x+8):
                for j in range(y,y+8):
                    if "WB"[((i+j)%2)^a] != m[i][j]: tmp += 1
            ans = min(ans,tmp)
print(ans)
