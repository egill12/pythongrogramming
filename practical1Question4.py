'''
Question 4 ........................................................ Total: 30 marks A mobile telephone company oﬀers two types of service: regular and premium. Its rates vary, depending on the type of service. The monthly rates are computed as follows: Regular service: £10.00 for the ﬁrst 50 minutes. Charges for over 50 minutes are 20 pence per minute. Premium service: £25.00 monthly charge plus a. for calls made from 6:00am to 6:00pm (daytime), the ﬁrst 75 minutes are free; charges for over 75 minutes are 10 pence per minute b. for calls made from 6:00pm to 6:00am (oﬀ-peak), the ﬁrst 100 minutes are free; charges for over 100 minutes are 5 pence per minute. Write a program to calculate and print mobile phone bills. The input is a series of records each giving the account number (a string), the customer surname, the balance on the account from last month, the type of service (R or P, for Regular or Premium, as explained below), followed by a single number of call minutes in the case of Regular service, and the number of daytime minutes and the number of oﬀ-peak minutes in the case of Premium customers.
BUCI033S7 Page 2 of 3 ©Birkbeck 2018
The ﬁle is terminated by a value of X0000 in place of an account number. A mini example input ﬁle, containing one of each type of record is
A9845 Hurley 37.35 R 55 A9846 Hicks 0.00 P 70 139 X0000
Your program should output, for each input record the account number, name, the type of service, the charge for the month, and the new balance on the account. Your program must declare, deﬁne and use functions to read each record, to compute regular charges, to compute premium charges, and to print each output record.

'''

def openfile(filename):
    '''
    Opens file of bill
    :param filename:
    :return:
    '''
    with open(filename) as f:
        return f.readlines()

def get_bills(data):
    '''
    Regular service: £10.00 for the ﬁrst 50 minutes. Charges for over 50 minutes a
    re 20 pence per minute. Premium service: £25.00 monthly charge plus a. for calls made
    from 6:00am to 6:00pm (daytime), the ﬁrst 75 minutes are free; charges for over
    75 minutes are 10 pence per minute b.
    for calls made from 6:00pm to 6:00am (oﬀ-peak), t
    he ﬁrst 100 minutes are free; charges for over 100 minutes are 5 pence per minute.
    :param data:
    :return:
    '''
    ACCOUNT_NUMBER = 0
    NAME = 1
    BALANCE = 2
    SERVICE = 3
    MINS = 4
    OFFPEAK = 5

    invoice = {}
    for bill in data:
        bill = bill.split()
        if bill[ACCOUNT_NUMBER] != "X000":
            if bill[SERVICE] == "R":
                # max(x) used to make sure we dont subtract money if minutes less than 50
                money_owed = 10 + max((0.2*(int(bill[MINS])-50)),0)
            elif bill[SERVICE] == "P":
                money_owed = 10 + max((0.1 * (int(bill[MINS]) - 75)), 0) + max((0.05 * (int(bill[OFFPEAK]) - 100)), 0)
            # add the data to the bill
            invoice[bill[ACCOUNT_NUMBER]] = dict(zip(['Name','Service','Charge','ME Balance'],[bill[NAME],bill[SERVICE],money_owed,money_owed]))
    return invoice




def main():
    filename = "bill.txt"
    # store the bill in data
    data = openfile(filename)
    print(data)
    # use function to get bill data
    phone_bill = get_bills(data)
    for key in phone_bill.keys():
        print(phone_bill[key])
main()