def cal(a,b):
    return a+b,a-b,a*b,a/b,a%b,a//b,a**b

v1=int(input('Enter first value:'))
v2=int(input('Enter the second value:'))
a,s,m,d,mo,fl,c=cal(v1,v2)
print('add=',a)
print('sub=',s)
print('mul=',m)
print('div=',d)
print('mod=',mo)
print('floor=',fl)
print('power=',c)
