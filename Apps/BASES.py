def h():
  print('db(n) : (decimal to binary)')
  print('bd(b) : (binary to decimal)')
def db(n): return bin(n).replace("0b", "")
def bd(n): return int(n, 2)