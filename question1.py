def fibonacci(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# up to and exclusive of 10
for i in range(0,10):
    print(fibonacci(i), end = " ")

for i in range(0,5):
    print(fibonacci(i), end = " ")
print(i)