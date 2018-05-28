def fibonacci(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(0,20):
    print(fibonacci(i), end = " ")

for i in range(0,2000):
    print(fibonacci(i), end = " ")
print(i)