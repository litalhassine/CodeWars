def mat_mul(m, n):
  a = m[0][0]*n[0][0] + m[1][0]*n[1][0]
  b = m[0][0]*n[1][0] + m[1][0]*n[1][1]
  c = m[1][0]*n[0][0] + m[1][1]*n[1][0]
  d = m[1][0]*n[0][1] + m[1][1]*n[1][1]

  m[0][0] = a
  m[0][1] = b
  m[1][0] = c
  m[1][1] = d

def neg_fib(n):
  a,b=0,1
  n_sign = n/abs(n)
  	
  for i in xrange(2, n*n_sign+1):
    new_val = a+n_sign*b
    a = b
    b = new_val

  return b  

def fib(n):
  """Calculates the nth Fibonacci number"""
  if n==0: return 0
  if n==1: return 1
  if n>1500000: return 0
  if n<0:
    return neg_fib(n)
      
  
  fib = [[1,1],[1,0]]
  res = [[1,0],[0,1]]
  
  while n>0:
    if (n%2 == 1): #n is odd
      mat_mul(res,fib)
    # n is even
    n = n/2
    mat_mul(fib,fib)

  return res[1][0]


  return res[1][0]



