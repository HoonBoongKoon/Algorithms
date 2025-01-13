while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    if a>b:
        if a>c:
            if a*a == (b*b)+(c*c):
                print('right')
            else:
                print('wrong')
        elif c>a:
            if c*c == (a*a)+(b*b):
                print('right')
            else:
                print('wrong')
    else:
        if b>c:
            if b*b == (a*a)+(c*c):
                print('right')
            else:
                print('wrong')
        elif c>b:
            if c*c == (a*a)+(b*b):
                print('right')
            else:
                print('wrong')
