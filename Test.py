
import math

test = int(input())
for i in range(test):
  num = int(input())
  lis = []
  data = num // 2
  print(data)
  lis.append(1)
  for itr in range(2,data+1):
      if num % itr == 0:
          lis.append(itr)
  lis.append(num)
  count = 1
  print(lis)
  for itr in range(1,len(lis)+1):
      count *= itr
  print(count)
  print(count-len(lis))
  result = len(lis)-2 + (len(lis))*(len(lis))
  print(result)
