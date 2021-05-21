from luhn import *
from os import system, name
import random
import datetime
import csv


def logo():
    print("   ______                       __   ______                  ")
    print(" .' ___  |                     |  ].' ___  |                 ")
    print("/ .'   \_| ,--.   _ .--.   .--.| |/ .'   \_|  .---.  _ .--.  ")
    print("| |       `'_\ : [ `/'`\]/ /'`\' || |   ____ / /__\\[ `.-. | ")
    print("\ `.___.'\// | |, | |    | \__/  |\ `.___]  || \__., | | | | ")
    print(" `.____ .'\'-;__/[___]    '.__.;__]`._____.'  '.__.'[___||__]")
    print("_____________________________________________________________")


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def genName():
    with open('names.csv', newline='') as csvfilename:
        with open('surnames.csv', newline='') as csvfilesur:
            readername = csv.reader(csvfilename)
            readersur = csv.reader(csvfilesur)
            dataname = list(readername)
            datasur = list(readersur)
            return random.choice(dataname)[0].capitalize(
            ) + " " + random.choice(datasur)[0].capitalize()


def genCard(firstDigits):
    res = str(firstDigits)
    k = 15 - len(res)
    for i in range(k):
        res += str(random.randint(0, 9))
    return (res + str(generate(res)),
            (str(random.randint(1, 12)).zfill(2) + '.' +
             str(datetime.datetime.now().year + random.randint(2, 5))[-2:]),
            str(random.randint(0, 9)) + str(random.randint(0, 9)) +
            str(random.randint(0, 9)))


def selectBank():
    clear()
    logo()
    print("Choose bank:")
    print("1.	Discover")
    print("2.	InstaPayment")
    print("3.	JCB")
    print("4.	Maestro")
    print("5.	MasterCard")
    print("6.	Visa")
    print("7.	Visa Electron")
    print("0.	Exit")
    i = input()
    if (i == "1"):
        return ("Discover", [6011] + list(range(622126, 622926)) +
                list(range(644, 650)) + [65] + [649])
    if (i == "2"):
        return ("InstaPayment", [637, 638, 639])
    if (i == "3"):
        return ("JCB", list(range(3528, 3590)))
    if (i == "4"):
        return ("Maestro",
                [5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763])
    if (i == "5"):
        return ("MasterCard",
                list(range(51, 56)) + list(range(222100, 272099)))
    if (i == "6"):
        return ("Visa", [4])
    if (i == "7"):
        return ("Visa Electron", [4026, 417500, 4508, 4844, 4913, 4917])
    if (i == "0"):
        return 0


i = 1
while i != "0":
    clear()
    logo()
    print("Select option:\n")
    print("1    Generate full credit card info")
    print("2.   Generate credit card number")
    print("3.   Generate name and surname")
    print("4.   Validate credit card number")
    print("0.   Exit")
    i = input()
    if (i == "1"):
        t = genCard(random.choice(selectBank()[1]))
        print("_____________________________________________________________")
        print(genName())
        print(t[0])
        print(t[1] + ' ' + t[2])
        input("Press any key to continue...")
    if (i == "2"):
        t = genCard(random.choice(selectBank()[1]))
        print("_____________________________________________________________")
        print(t[0])
        print(t[1] + ' ' + t[2])
        input("Press any key to continue...")
    if (i == "3"):
        print("_____________________________________________________________")
        print(genName())
        input("Press any key to continue...")
    if (i == "4"):
        print("_____________________________________________________________")
        t = input("Input card number:")
        print(verify(t))
        input("Press any key to continue...")
