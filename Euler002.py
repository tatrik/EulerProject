# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibonacci(d, k):
  for i in range(2, 50):
    a = l[i-1] + l[i-2]
    if a < 4000000:
      l.append(a)
      if a % 2 == 0:
        l_2.append(a)
      else:
        continue
    else:
      break
  s = sum(l_2)
  return s
l = [1 , 2]
l_2 = [2]
fibonacci(l, l_2)