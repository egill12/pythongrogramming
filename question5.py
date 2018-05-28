'''
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works

'''

def convert_to_set(list):
    return set(list)

def intersection(list1,list2):
    '''
    Take two lists, say for example these two:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b   = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only the elements that are
    common between the lists (without duplicates). Make sure your program works
    :param list1:
    :param list2:
    :return:
    '''
    set_list1 = convert_to_set(list1)
    set_list2 = convert_to_set(list2)
    return list(set_list1 & set_list2)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55, 12, 13]

print(intersection(a,b))