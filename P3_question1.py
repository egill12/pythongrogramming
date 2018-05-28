'''
Write a function that takes an ordered list of numbers (a list where the elements
are in order from smallest to largest) and another number. The function decides
whether or not the given number is inside the list and returns (then prints) an
appropriate boolean.
'''

def find_number(list,num):
    '''
    Write a function that takes an ordered list of numbers (a list where the elements
    are in order from smallest to largest) and another number. The function decides
    whether or not the given number is inside the list and returns (then prints) an
    appropriate boolean.

    :param list:
    :param num:
    :return:
    '''
    # find max index of the list
    index_max = len(list) -1
    # check if number is too small or too big to be in list
    if num > list[index_max] or num < list[0]:
        return  False
    for element in list:
            if num == element:
                return True
    return False

print(find_number([1,2,3,4],4))