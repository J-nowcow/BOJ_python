import re
import sys
input = sys.stdin.readline

p = list(map(int,input().split()))
d = {"+": p[0], "-": p[1], "*": p[2], "/": p[3]}

s = input()

num = list(map(str,map(int,re.split("[*+-/]", s))))
op = re.findall("[*+-/]",s)

dic = {}
for i in range(-1,len(num)):
    dic[i] = [i-1,i+1]

if len(num) == 1:
    print(int(num[0]))
else:
    a = 0
    for i in range(4,0,-1):
        tmp = len(op)
        for j in range(tmp-1,-1,-1):
            if d[op[j]] == i:
                if op[j] == "/":
                    if int(num[dic[j][1]]) > 0 and int(num[j]) > 0:
                        z = "+"
                    elif int(num[dic[j][1]]) < 0 and int(num[j]) < 0:
                        z = "+"
                    else:
                        z = "-"

                    if z == "-":
                        cal = "-" + str((abs(int(num[dic[j][1]]))//(abs(int(num[j])))))
                    else:
                        cal = str((abs(int(num[dic[j][1]]))//(abs(int(num[j])))))
                elif op[j] == "+":
                    cal = str(int(num[dic[j][1]])+int(num[j]))
                elif op[j] == "-":
                    cal = str(int(num[dic[j][1]])-int(num[j]))
                elif op[j] == "*":
                    cal = str(int(num[dic[j][1]])*int(num[j]))
                num[j] = cal
                num[dic[j][1]] = cal
                dic[dic[j][0]][1] = dic[j][1]
                dic[dic[j][1]][0] = dic[j][0]
                a = j
    
    print(int(num[dic[a][1]]))
