a=int(input())
b=int(input())
c=int(input())
if(1<=a<=100 and 1<=b<=100 and 1<=c<=100):
    if(a+b==c or a+c==b or b+c==a):
        print("Yes")
    else:
        print("No")
