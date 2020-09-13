"""
KMP 알고리즘을 활용한 문제

prefix = suffix가 되는 문자열의 최대 길이를 구하면 된다.
만약 20자리 문자열에서 처음 7자리랑 끝에 7자리가 겹친다면 13자리 광고일 때 이 문자열을 표현할 수 있다.

"""
a=input
L = int(a())
s = a()

t = [0]*L
j = 0
for i in range(1,L):
    while j > 0 and s[i] != s[j]:
        j = t[j-1]
    if s[i] == s[j]:
        j += 1
        t[i] = j
print(L-t[-1])
