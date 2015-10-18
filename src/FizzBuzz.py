
__author__ = 'Garrett LaRue'

def decToHex():
    strIntNumber = input("enter a decimal number>> ")
    intHex = int(strIntNumber, 10)
    strHex = hex(intHex)
    print(strIntNumber + " in Hexadecimal is " + strHex)
    input("press enter to continue..\n")
    return strHex

def hexToDec():
    strHexNumber = input("enter a hexadecimal number>> ")
    intDec = int(strHexNumber, 16)
    strDec = str(intDec)
    print(strHexNumber + " in Decimal is " + strDec)
    input("press enter to continue..\n")
    return strDec

def helloWorld():
    print("Hello, world!\n")
    input("press enter to continue..\n")

def countToTen():
    print("counting from 1 to 10:")
    for count in range(1,11):
        print("{}".format(count))
    input("press enter to continue..\n")

def fizzBuzz():
    print("FizzBuzz counter:")
    for iterator in range(1,101):
        if iterator % 3 == 0 and iterator % 5 == 0:
            print("{}:FizzBuzz!".format(iterator))
        elif iterator % 3 == 0:
            print("{}:Fizz".format(iterator))
        elif iterator % 5 == 0:
            print("{}:Buzz".format(iterator))
        else:
            print("{}".format(iterator))
    input("press enter to continue..\n")

def greet():
    choice = ""
    greeting = """
    Welcome to Garrett's FizzBuzz Demo
    Inspired by "Why Can\'t Programmers.. Program?"
    http://blog.codinghorror.com/why-cant-programmers-program/

    Choose a demo to view:
    1: Hello World
    2: Count to Ten
    3: FizzBuzz
    4: Decimal to Hexadecimal
    5: Hexadecimal to Decimal
    6: Quit

    """
    while choice != "6":
        print(greeting)
        choice = input(">> ")
        if choice == "1":
            helloWorld()
        elif choice == "2":
            countToTen()
        elif choice == "3":
            fizzBuzz()
        elif choice == "4":
            decToHex()
        elif choice == "5":
            hexToDec()
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print(greeting)

greet()
