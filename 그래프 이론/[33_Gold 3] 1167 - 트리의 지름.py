"""
트리의 지름 구하기
① 임의의 한 노드에서 가장 먼 노드 찾기
② 그 노드에서 가장 먼 노드까지의 거리가 트리의 지름
"""
import queue
import sys
input = sys.stdin.readline

V = int(input())
dic = {i:set() for i in range(1,V+1)}
for _ in range(V):
    dist = list(map(int, input().split()))
    i = dist[0]
    dist = dist[1:-1]
    for j in zip(dist[::2],dist[1::2]):
        dic[i].add(j)

def bfs(start):    
    check = [-1]*(V+1)
    q = queue.Queue()
    q.put((start,0))
    check[start] = 0
    while not q.empty():
        a,b = q.get()
        for i in dic[a]:
            if check[i[0]] == -1 or check[i[0]] > b + i[1]:
                check[i[0]] = b + i[1]
                q.put((i[0], b + i[1] ))
    m = max(check)
    return check.index(max(check)), m

a,b = bfs(1)
print(bfs(a)[1])
