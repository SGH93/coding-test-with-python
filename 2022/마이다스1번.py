def solution(H):
  mh = 1
  idx = 0
  cnt = 0
  answer = []
  while mh <= max(H):
      while idx < len(H):
          for i in range(idx, len(H)):
              if H[i] < mh:
                  break
              if H[i] == mh:
                  for j in range(i, len(H)):
                      if H[j] < mh:
                          break
                      print(idx, i, j)  
                      cnt += 1
                  break                      
          idx += 1
      if cnt > 0:
          answer.append([mh, cnt])
      cnt = 0
      idx = 0
      mh += 1
  return answer
  
def solution2(H):
  mh = 1
  idx = 0
  cnt = 0
  answer = []
  for MaxHight in range(1, max(H)+1):
    for idx in range(len(H)):
      for i in range(idx, len(H)):
          if H[i] < MaxHight:
            break
          if H[i] == mh:
            for j in range(i, len(H)):
              if H[j] < MaxHight:
                break
              print(idx, i, j)  
              cnt += 1
            break                      
    if cnt > 0:
        answer.append([MaxHight, cnt])
    cnt = 0
  return answer




print(solution2([3,2,1,1,3]))

