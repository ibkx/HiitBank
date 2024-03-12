
import random
class account:
    def __init__(self, fname, lname, phone_no, email, pin, passcode, address, bvn, balance,nin):
        self.__fname = fname
        self.__lname = lname
        self.__phone_no = None
        self.__email = email
        self.__pin = pin
        self.__passcode = passcode
        self.__address:str = None


        if bvn == None:
            self.bvn = str(random.randint(100000000000, 99999999999))
        else:
            self.__bvn = bvn


        self.__balance = balance
        self.__nin = nin

    def get_fname(self):
        return self.__fname

    def get_lname(self):
        return self.__lname

    def get_nin(self):
        return self.__nin

    def get_balance(self):
        return self.__balance



    def withdraw(self, amount:float):
        assert type(amount) == float, "Amount to withdraw must be a number"
        assert amount > 0, "Amount to withdraw must be a positive number"
        assert amount < self.__balance, "Insufficient funds"

        self.__balance = amount
        return self.__balance


    def deposit(self, amount:float):
        assert type(amount) == float, "Amount to deposit must be a number"
        assert amount > 0, "Amount to deposit must be a positive number"

        self.__deposit = amount
        return self.__deposit
