# 아홉 난쟁이 중 일곱 명의 키의 합이 100이 되는 경우 찾기
a = [int(input()) for _ in range(9)]
c = False
for i in range(9):
    for j in range(i+1,9):
        if sum(a) - a[i] - a[j] == 100:
            c = True
            b = sorted(a[:i] + a[i+1:j] + a[j+1:])
            for k in b: print(k)
            break
    if c:
        break
        
