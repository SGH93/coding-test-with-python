s = int(input())
cnt  = 0
n = 1
while True:
  s -= n
  cnt += 1
  if s <= n:
    break
  n += 1
  


print(cnt)