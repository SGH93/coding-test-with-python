def solution(money, costs):
  coins = [1, 5, 10, 50, 100, 500]
  cnt = [0, 0, 0, 0, 0, 0]  
  answer = 0  

  efficiency = {}
  for i in range(len(coins)):
    efficiency[coins[i]] = coins[i]/costs[i]
  efficiency = dict(sorted(efficiency.items(), key = lambda x:(x[1], x[0]), reverse = True))
  
  while True:
    if money == 0:
      break
    for i in efficiency.keys():
      if(i <= money):
        cnt[coins.index(i)] = money//i
        money = money%i
        print(i, cnt[coins.index(i)], money)
        continue

  for i in range(len(costs)):
    answer = answer + (costs[i]*cnt[i])
  return answer


def solution2(money, coins, efficiency):
  cnt = [0, 0, 0, 0, 0, 0]  
  while True:
    if money == 0:
      return cnt
    else:
      for i in efficiency.keys():
        if(i <= money):
          cnt[coins.index(i)] = money//i
          money = money%i
          print(i, cnt[coins.index(i)], money)
          solution2(money, coins, efficiency)


        

print(solution(4578, [1, 4, 99, 35, 50, 1000]))

