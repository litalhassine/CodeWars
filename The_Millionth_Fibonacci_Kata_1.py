def fib(n):
  """Calculates the nth Fibonacci number"""
  if n==0: return 0
  if n>1500000: return 0
  
  a=0
  b=1
  n_sign = n/abs(n)

  for i in xrange(2, n*n_sign+1):
      new_val = a+n_sign*b
      a = b
      b = new_val
  
  return b


