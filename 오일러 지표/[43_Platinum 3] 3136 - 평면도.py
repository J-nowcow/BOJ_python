"""
프로그래머스 그래프 문제인 '방의 개수'와 동일한 문제
"""
int(input())
arrows = input()

x = y = 0 # 현재 좌표
edge = set(); node = set([(0,0)]) # 간선 저장할 집합, 꼭짓점 저장할 집합
# x: 0,1,7: 증가, 2,6: 유지, 3,4,5: 감소
# y: 1,2,3: 증가, 0,4: 유지, 5,6,7: 감소

for i in arrows:
    i = int(i)
    a = (int((i+1) % 8 < 3) - int(3 < (i+1) % 8 < 7))
    b = (int(0 < i < 4) - int(4 < i))
    
    # 집합에 꼭짓점 추가
    node.update([(x+a,y+b), (x+a*2,y+b*2)])
    # 집합에 간선 추가
    edge.update([(x,y,x+a*2,y+b*2),(x+a*2,y+b*2,x,y)])
    x += a*2; y += b*2

print(len(edge) - len(node) + 1)
