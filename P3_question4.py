'''
Write a program that asks the user for a long string containing multiple words.
Echo back to the user the same string, except with the words in backwards order.
For example, say we type the string:
My name is Michele
Then we would expect to see the string:
Michele is name My

'''

def reverse_str(string):
    '''
    Write a program that asks the user for a long string containing multiple words.
    Echo back to the user the same string, except with the words in backwards order.
    :param string:
    :return:
    '''
    broken_string = string.split()
    reversed_string = []
    for element in reversed(broken_string):
        reversed_string.append(element)
    return reversed_string


string = str(input("please give str:"))
reversed_string = reverse_str(string)

for element in reversed_string:
    print(element, end = " " )