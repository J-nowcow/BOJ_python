"""
dp 문제중 가장 기초적인 문제

N짜리 리스트를 만든 다음, 리스트에 이 값을 만들기 위해 몇 번의 연산을 했는지 기록한다.
재귀로 구현해도 되고 queue에 넣어도 된다.

근데 import queue하니까 시간초과 
"""

N = int(input())
q = [(N,0)]

lst = [-1]*(N+1)
lst[N] = 0

idx = 0
while True:
    tmp, check = q[idx]
            
    if tmp == 1:
        print(check)
        break
    
    if tmp % 3 == 0 and lst[tmp // 3] == -1:
        lst[tmp // 3] = check + 1
        q.append((tmp//3, check+1))
    if tmp % 2 == 0 and lst[tmp // 2] == -1:
        lst[tmp // 2] = check + 1
        q.append((tmp//2, check+1))
    if lst[tmp - 1] == -1:
        lst[tmp-1] = check + 1
        q.append((tmp-1, check+1))

    idx += 1
