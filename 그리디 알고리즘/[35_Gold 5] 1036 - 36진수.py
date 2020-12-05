"""
1부터 Z까지 36개의 딕셔너리 생성
각 딕셔너리에 1부터 50까지 각 자리수에 그 문자가 몇 번 나오는지 저장
"""
ch = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d = {i : [0]*50 for i in ch}

N = int(input())

for _ in range(N):
    tmp = input()
    for i,c in enumerate(tmp):
        d[c][len(tmp) - (i+1)] += 1

order = []
t = [1]
for i in range(49):
    t.append(t[-1]*36)

for i in range(36):
    tmp = 0
    for j in range(50):
        tmp += t[j] * d[ch[i]][j]
    order.append((i,(35-i) * tmp))

order.sort(key = lambda x: x[1], reverse = True)

k = int(input())
change = []
for i in order[:k]:
    change.append(i[0])


ans = [0] * 52
for i in range(36):
    for j in range(50):
        if i in change:
            ans[j] += 35 * d[ch[i]][j]
        else:
            ans[j] += i * d[ch[i]][j]

for i in range(51):
    ans[i+1] += ans[i] // 36
    ans[i] %= 36

answer = ""
check = False
for i in ans[::-1]:
    if i == 0 and check == False:
        continue
    check = True
    answer += ch[i]

if answer == "":
    print("0")
else:
    print(answer)
