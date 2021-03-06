'''
Create a program that will play the “cows and bulls” game with the user. The
game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a
“cow”. For every digit the user guessed correctly in the wrong place is a “bull”.
Every time the user makes a guess, tell them how many “cows” and “bulls” they
have. Once the user guesses the correct number, the game is over. Keep track of
the number of guesses the user makes throughout the game and tell the user at
the end.
Say the number generated by the computer is 1038. An example interaction
could look like this:
BUCI033S7 Page 2 of 3 ©Birkbeck 2018
Welcome to the Cows and Bulls Game!
Enter a number:
 1234
2 cows, 0 bulls 1256
1 cow, 1 bull
...
Until the user guesses the number.


'''
import random


def check_guess(guess,random_number):
    '''
    Check that guess is not correct
    :param guess:
    :param random_number:
    :return:
    '''
    return guess == random_number

def convert_to_list(number):
    '''

    :param number:
    :return:
    '''
    storage_list = []
    for char in number:
        storage_list.append(char)
    return storage_list

def cows_bulls(guess,random_number):
    '''
    or every digit that the user guessed correctly in the correct place, they have a
    “cow”. For every digit the user guessed correctly in the wrong place is a “bull”.
    Every time the user makes a guess, tell them how many “cows” and “bulls” they
    have. Once the user guesses the correct number, the game is over. Keep track of
    the number of guesses the user makes throughout the game and tell the user at
    the end.

    :param guess:
    :param random_number:
    :return:
    '''
    guess = convert_to_list(guess)
    print(guess)
    number = convert_to_list(random_number)
    print(number)
    cows = 0
    bulls = 0
    for index_guess in range(0,len(guess)):
        #
        if guess[index_guess] in random_number:
            bulls += 1
            #
            for index_random in range(0,len(guess)):
                #
                if guess[index_guess] == number[index_random] and index_guess == index_random:
                    cows += 1
    # I count all bulls first, then find out how many cows there were, t fiund bulls i need to subtract the number of cows found..
    return (cows, bulls-cows)


random_number = random.randint(1000,9999)
# initial value
guess = -1
COW_INDEX = 0
BULL_INDEX = 1
iterations = 0
while not check_guess(guess,random_number):
    iterations += 1
    guess = str(input("Please enter your guess:"))
    cows_bulls_score = cows_bulls(guess,random_number)
    print("You had %s cows and %s bulls" %(str(cows_bulls_score[COW_INDEX]), str(cows_bulls_score[BULL_INDEX])))

print("Congrats you did it! That took %s goes" % str(iterations))