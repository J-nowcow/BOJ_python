for i in "A"*int(input()):
    a,b,c = map(int,input().split())
    print("%d%02d"%((c-1)%a+1,(c-1)//a+1))
