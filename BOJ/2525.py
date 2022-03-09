h, m = map(int, input().split())
t = int(input())

n = m+t

h = h + n//60
m = n%60

if h >= 24:
  h = h-24
  
print(str(h) + " "+ str(m))