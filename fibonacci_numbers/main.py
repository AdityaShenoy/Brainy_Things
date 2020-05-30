'''
Fibonacci numbers
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

F(n) = F(n - 1) + F(n - 2)
F(0) = 0
F(1) = 1
'''

def fibo(n):
  return fibo_memo(n, dict())

def fibo_memo(n, dp):
  if n in dp:
    return dp[n]
  if n in [0, 1]:
    dp[n] = n
  else:
    dp[n] = fibo_memo(n - 1, dp) + fibo_memo(n - 2, dp)
  return dp[n]