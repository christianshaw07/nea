import sqlite3
import tkinter


class CashRegister:
    def __init__(self, one_pence_count, two_pence_count, five_pence_count, ten_pence_count,twenty_pence_count, fifty_pence_count,
                 one_pound_count, two_pound_count, five_pound_count, ten_pound_count, twenty_pound_count,
                 fifty_pound_count):
        self.one_pence_count = one_pence_count
        self.two_pence_count = two_pence_count
        self.five_pence_count = five_pence_count
        self.ten_pence_count = ten_pence_count
        self.twenty_pence_count = twenty_pound_count
        self.fifty_pence_count = fifty_pence_count
        self.one_pound_count = one_pound_count
        self.two_pound_count = two_pound_count
        self.five_pound_count = five_pound_count
        self.ten_pound_count = ten_pound_count
        self.twenty_pound_count = twenty_pound_count
        self.fifty_pound_count = fifty_pound_count

    def display_cash(self):
        penny_count = 0
        penny_count += (self.one_pence_count * 1)
        penny_count += (self.two_pence_count * 2)
        penny_count += (self.five_pence_count * 5)
        penny_count += (self.ten_pence_count * 10)
        penny_count += (self.fifty_pence_count * 50)
        penny_count += (self.one_pound_count * 100)
        penny_count += (self.two_pound_count * 200)
        penny_count += (self.five_pound_count * 500)
        penny_count += (self.ten_pound_count * 1000)
        penny_count += (self.twenty_pound_count * 2000)
        penny_count += (self.fifty_pound_count * 5000) #5000 pennies in 50 pounds

        #work out how many pounds there are
        pound_count = penny_count // 100

        #the remainder, is the amount of pence
        penny_count = penny_count % 100

        return f'£{pound_count}.{penny_count}'

    def money_in(self,money_count,money_type):
        if money_type == '1p':
            self.one_pence_count += money_count
        elif money_type == '2p':
            self.two_pence_count += money_count
        elif money_type == '5p':
            self.five_pence_count += money_count
        elif money_type == '10p':
            self.ten_pence_count += money_count
        elif money_type == '20p':
            self.twenty_pence_count += money_count
        elif money_type == '50p':
            self.fifty_pence_count += money_count
        elif money_type == '£1':
            self.one_pound_count += money_count
        elif money_type == '£2':
            self.two_pound_count += money_count
        elif money_type == '£5':
            self.five_pound_count += money_count
        elif money_type == '£10':
            self.ten_pound_count += money_count
        elif money_type == '£20':
            self.twenty_pound_count += money_count
        elif money_type == '£50':
            self.fifty_pound_count += money_count
        else:
            print("Invalid money type")

    def money_out(self,amount_due): #pass this through in pence  
        while amount_due != 0:
            if amount_due // 2000 != 0: #if there is enough change that we can get a 20 pound note out
                twenty_pound_out = amount_due / 2000
                amount_due -= 2000 * int(twenty_pound_out)
                self.twenty_pound_count -= int(twenty_pound_out)

            if amount_due // 1000 != 0: #if there is enough change that we can get a 10 pound note out
                ten_pound_out = amount_due / 1000
                amount_due -= 1000 * int(ten_pound_out)
                self.ten_pound_count -= int(ten_pound_out)

            if amount_due // 500 != 0: #if there is enough change that we can get a 5 pound note out
                five_pound_out = amount_due / 500
                amount_due -= 500 * int(five_pound_out)
                self.five_pound_count -= int(five_pound_out)

            if amount_due // 200 != 0: #if there is enough change that we can get a 2 pound coin out
                two_pound_out = amount_due / 200
                amount_due -= 200 * int(two_pound_out)
                self.two_pound_count -= int(two_pound_out)

            if amount_due // 100 != 0: #if there is enough change that we can get a 1 pound coin out
                one_pound_out = amount_due / 100
                amount_due -= 100 * int(one_pound_out)
                self.one_pound_count -= int(one_pound_out)

            if amount_due // 50 != 0: #if there is enough change that we can get a 50p coin out
                fifty_pence_out = amount_due / 50
                amount_due -= 50 * int(fifty_pence_out)
                self.fifty_pence_count -= int(fifty_pence_out)

            if amount_due // 20 != 0: #if there is enough change that we can get a 20p coin out
                twenty_pence_out = amount_due / 20
                amount_due -= 20 * int(twenty_pence_out)
                self.twenty_pence_count -= int(twenty_pence_out)

            if amount_due // 10 != 0: #if there is enough change that we can get a 10p coin out
                ten_pence_out = amount_due / 10
                amount_due -= 10 * int(ten_pence_out)
                self.ten_pence_count -= int(ten_pence_out)

            if amount_due // 5 != 0: #if there is enough change that we can get a 5p coin out
                five_pence_out = amount_due / 5
                amount_due -= 5 * int(five_pence_out)
                self.five_pence_count -= int(five_pence_out)

            if amount_due // 2 != 0: #if there is enough change that we can get a 2p coin out
                two_pence_out = amount_due / 2
                amount_due -= 2 * int(two_pence_out)
                self.two_pence_count -= int(two_pence_out)

            if amount_due // 1 != 0: #if there is enough change that we can get a 1p coin out
                one_pence_out = amount_due / 1
                amount_due -= 1 * int(one_pence_out)
                self.one_pence_count -= int(one_pence_out)
        
#Example usage
tesco_cash_register = CashRegister(0,0,0,0,0,0,0,0,0,0,0,1)
tesco_cash_register.money_in(5,'£50')
print(tesco_cash_register.display_cash())
tesco_cash_register.money_out(5000)
print(tesco_cash_register.display_cash())



