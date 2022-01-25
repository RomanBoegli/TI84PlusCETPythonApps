def h():
  print('phi(n) : (number of co-primes)')
  print('gcd(x, y) : (gcd)')
  print('mod(x, y) : (remainder)')
def phi(n): return sum([gcd(n, k)==1 for k in range(1, n+1)])
def gcd(x, y):
    if(y==0): return x
    else: return gcd(y,x%y)
def mod(x, y): return x % y