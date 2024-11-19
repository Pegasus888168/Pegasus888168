a = 0
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
          print(n, 'equals', x, '*', n//x)
          break
    else:
         # loop fell through without finding a factor
        a=a+1
        print(n, 'is a prime number')
        
print('TTL:', a, 'PRIME numbers')
