"""
트리의 말단 노드부터 탐색하기 : 재귀함수로 구현
말단 노드 = return 0

자식 노드들의 dp값을 가져와서 가장 오래 걸리는 자식 노드부터 처리
[5,4,3,2] 라면 1 + 5초
[5,5,4,3] 이라면 1 + (5+1)초
[5,5,5,4,3] 이라면 1 + (5+2)초
[5,4,4,4] 라면 1+5초라고 생각할 수 있지만 4때문에 더 오래걸림

--> 정렬하고 가장 작은 숫자부터 보기
n-1번 째 수가 n번 째 수와 같거나 더 크다면 tmp[n] = tmp[n-1] + 1
[4,4,4,5] -> [4,5,6,7]

"""

def fun(node):
    # 말단 노드인 경우
    if not tree[node]:
        dp[node] = 0
        return 0

    tmp = []
    for i in tree[node]:
        if dp[i] == -1:
            fun(i)
        tmp.append(dp[i])
    tmp.sort()
    for i in range(1,len(tmp)):
        if tmp[i] <= tmp[i-1]:
            tmp[i] = tmp[i-1] + 1
    dp[node] = tmp[-1] + 1
    return dp[node]

N = int(input())
lst = map(int, input().split())

tree = {i:[] for i in range(N)}
dp = [0] + [-1] * (N-1)
for i, boss in enumerate(lst):
    if boss == -1: continue
    tree[boss].append(i)

print(fun(0))
