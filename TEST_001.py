# Fibonacci series:
# the sum of two elements defines the next
a, b, c = 0, 1, 0
while a < 1000:
     c = c+1
     print(a, end=", ")
     a, b = b, a+b

print("總共:",c,"個")