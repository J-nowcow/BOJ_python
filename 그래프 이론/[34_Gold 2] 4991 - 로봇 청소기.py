# pypy3으로 제출된 코드입니다
"""
더러운 칸 청소하기
칸의 개수 최대 10개 -> 10! = 3628800
모든 조합에 대해 거리 계산해보고 최솟값으로 가기

dp[i][j] = 0으로 두고 주변 한칸씩 늘려가면서 거리 찾아주기: bfs
"""

import itertools

while True:
    x,y = map(int,input().split())
    # 모든 테케 끝났으면 break
    if x == 0: break
    
    board = [input() for _ in range(y)]

    # 더러운 칸의 수
    dust = []
    for i in range(y):
        for j in range(x):
            if board[i][j] == "*":
                dust.append((i,j))
            elif board[i][j] == "o":
                robot = (i,j)
                
    dust = [robot] + dust
    way = ((-1,0),(1,0),(0,-1),(0,1))

    dist = [[0]*len(dust) for _ in range(len(dust))]

    # 각 더러운 칸과 출발지점들 간의 거리 구하기: bfs 활용
    for start in range(len(dust)):
        dp = [[-1]*x for _ in range(y)]
        dp[dust[start][0]][dust[start][1]] = 0
        lst = [dust[start]] # 거리 x인 점들의 집합: 거리 0인 초기 위치만 넣어주기
        distance = 1
        while True:
            tmp = []
            for pos in lst:
                for w in way:
                    a = pos[0]+w[0]; b = pos[1]+w[1]
                    if 0 <= a < y and 0 <= b < x and board[a][b] != "x" and dp[a][b] == -1:
                        dp[a][b] = distance
                        tmp.append((a,b))
            if not tmp: break
            lst = tmp
            distance += 1

        # 거리 업데이트
        tmp = True
        for end in range(len(dust)):
            # 거리가 -1: 연결되지 않은 점이 존재 -> 불가능
            if dp[dust[end][0]][dust[end][1]] == -1:
                tmp = False; break
            dist[start][end] = dp[dust[end][0]][dust[end][1]]
        if tmp == False: break
    if tmp == False:
        print(-1)
        continue

    answer = float("inf")
    # 각 순서별로 값 구하기
    for order in itertools.permutations(range(1,len(dist))):
        tmp = dist[0][order[0]]
        for i,j in zip(order,order[1:]):
            tmp += dist[i][j]
        answer = min(answer, tmp)
    print(answer)
