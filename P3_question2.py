'''
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
'''



def is_prime(number):
    '''
    Determines whether the number is prime or not.
    :param number:
    :return:
    '''
    is_prime = True
    for i in range(2,num):
        if (num % i) == 0:
            is_prime = False
    return is_prime

num = int(input("Enter number :"))

print(is_prime(num))