t = int(input())
for _ in range(t):
  m = list(input().split())
  num = float(m.pop(0))
  for i in range(len(m)):
    if m[i] == "#":
        num -= 7
    elif m[i] == "%":
        num += 5
    elif m[i] == "@":
        num *= 3
  print("%0.2f" % num)