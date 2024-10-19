import random
import time
import os
import subprocess

try:
    import colorama
    from colorama import Fore, Back, Style
except ImportError:
    os.system('pip install colorama')
    import colorama
    from colorama import Fore, Back, Style

try:
    from art import text2art
except ImportError:
    os.system('pip install art')
    from art import text2art

colorama.init()

os.system('clear')

class validator():

    def __init__(self):
        self.cardNumber = None
        self.Brand = None

    def __findBrand(self):
        if self.cardNumber[:2] in ['34', '37']:
            self.Brand = 'American Express'
        elif self.cardNumber[:3] in ['300', '301', '302', '303', '304', '305']:
            self.Brand = 'Diners Club - Carte Blanche'
        elif self.cardNumber[:2] in ['36']:
            self.Brand = 'Diners Club - International'
        elif self.cardNumber[:2] in ['54']:
            self.Brand = 'Diners Club - USA & Canada'
        elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648',
                                                                         '649'] or self.cardNumber[0:2] in [
            '65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif self.cardNumber[:3] in ['637', '638', '639']:
            self.Brand = 'InstaPayment'
        elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
            self.Brand = 'Maestro'
        elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in
                                                                                              range(222100, 272100)]:
            self.Brand = 'MasterCard'
        elif self.cardNumber[:4] in ['4026', '4508', '4844', '4913', '4917'] or self.cardNumber[:6] == '417500':
            self.Brand = 'VISA Electron'
        elif self.cardNumber[0] in ['4']:
            self.Brand = 'VISA'
        else:
            self.Brand = 'Unknown Brand'

    def validate(self, number):
        """
        number: str or int credit card number
        """
        if number is None: return 'Not a valid Credit Card Number'
        if number is bool: return 'Not a valid Credit Card Number'
        if number is float: return 'Not a valid Credit Card Number'
        number = ''.join(x for x in str(number).strip().split())
        if number.isdigit() and 13 <= len(number) <= 19:
            self.cardNumber = number
            self.__findBrand()
            lastDigit = int(number[-1])
            base = [int(x) for x in reversed(number[:-1])]
            base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
            base = [x if x <= 9 else x - 9 for x in base]
            base = sum(base)
            base = (base * 9) % 10
            if base == lastDigit:
                print(Fore.GREEN)
                return f'[!] VALID | {self.cardNumber}'
                file = open("Cards.txt", "w")
                number = repr(number)
                file.write(number)
                file.close()
            else:
                print(Fore.RED)
                return f'[?] INVALID | {self.cardNumber}'
        else:
            return 'Not a valid Credit Card Number'
os.system('clear')
banner = text2art("Card  Generator")
print(Fore.GREEN + banner)
print('Card Types:')
print('0.  < $1000 Amazon Storecard')
print('1.  $1000 Amazon Storecard')
print('2.  $2000 Amazon Storecard')
print('3.  $5000 Amazon Storecard')
print('4.  $7000 Amazon Storecard')
print('5.  $10.000 Amazon Storecard')
print('6.  $20.000 Amazon Storecard')
print('7.  $40.000 Amazon Storecard')
print('8.  $100.000 Amazon Storecard')
print('9.  Amazon Corporate Revolving Storecard')
print('10. Multifunction Discover Card')
print('11. BestBuy Storecard')
print('12. Target Storecard')
print('13. Amazon Visa Signature Credit Card')
print('14. Random Amazon Storecard $0-$10.000')
print('15. HQ BestBuy Storecard')
print('16. HQ Multifunction Discover Card')
print('17. EXIT')
print(' ')
whatcard = input(Fore.YELLOW + "[?] What card type you want to generate: ")

whatcard = int(whatcard)
randomnums = "0123456789"

if whatcard == 1:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    time.sleep(0.8)
    time.sleep(0.8)
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811425'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))
if whatcard == 2:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578114'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7)
        print(validator().validate(int(cc)))
if whatcard == 3:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578118'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7)
        print(validator().validate(int(cc)))
if whatcard == 4:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578114860'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4)
        print(validator().validate(int(cc)))
if whatcard == 5:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '6045781123'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6)
        print(validator().validate(int(cc)))
if whatcard == 6:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811496'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))
if whatcard == 7:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811436'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))
if whatcard == 8:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811318'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))
if whatcard == 0:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578112729'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4)
        print(validator().validate(int(cc)))
if whatcard == 9:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '604578172729'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4)
        print(validator().validate(int(cc)))
if whatcard == 10:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '601100351312'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4)
        print(validator().validate(int(cc)))
if whatcard == 11:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '702126'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        ff9 = random.choice(randomnums)
        ff10 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7) + str(ff8) + str(ff9) + str(ff10)
        print(validator().validate(int(cc)))
if whatcard == 12:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '5859752142'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6)
        print(validator().validate(int(cc)))
if whatcard == 13:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '414840'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        ff9 = random.choice(randomnums)
        ff10 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7) + str(ff8) + str(ff9) + str(ff10)
        print(validator().validate(int(cc)))
if whatcard == 14:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '60457811'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7) + str(ff8)
        print(validator().validate(int(cc)))
if whatcard == 15:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '5859752142'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6)
        print(validator().validate(int(cc)))
if whatcard == 16:
    howmany = input('[?] How many cards do you want to generate and check (recommended 100): ')
    howmany = int(howmany)
    for x in range(howmany):
        bin = '601120'
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        ff6 = random.choice(randomnums)
        ff7 = random.choice(randomnums)
        ff8 = random.choice(randomnums)
        ff9 = random.choice(randomnums)
        ff10 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5) + str(ff6) + str(ff7) + str(ff8) + str(ff9) + str(ff10)
        print(validator().validate(int(cc)))
if whatcard == 17:
    os.system('clear')
