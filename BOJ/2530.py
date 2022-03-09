a, b, c = map(int, input().split())
d =int(input())

c = c+d

if(c >= 60):
  b = b+c//60
  c = c%60
  if(b>=60) :
    a = a+b//60
    b = b%60
    if(a >= 24):
      a = a%24

print(str(a)+" "+str(b)+" "+str(c))

h,m,s=map(int,input().split())
s+=int(input())
m+=s//60
print((h+m//60)%24,m%60,s%60)