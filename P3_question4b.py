'''
Write a program that asks the user how many Fibonacci numbers to generate and
then generates them. Make sure to ask the user to enter the number of numbers
in the sequence to generate. (Hint: The Fibonacci sequence is a sequence of
numbers where the next number in the sequence is the sum of the previous two
numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, . . . )
'''

# creating fib function
def fib(n):
    '''
    The Fibonacci sequence is a sequence of
    numbers where the next number in the sequence is the sum of the previous two
    numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, . . . )

    :param n:
    :return:
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

no_numbers = int(input("How many Fibs do you want?"))

for i in range(0,no_numbers):
    print(fib(i))
