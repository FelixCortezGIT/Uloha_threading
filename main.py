import threading

user = input("zadaj cisla oddelene medzerou: ")
numbers = list(map(int, user.split()))

def find_max():
    maximum = max(numbers)
    print("najvyssie cislo: ", maximum)

def find_min():
    minimum = min(numbers)
    print("najnizsie cislo: ", minimum)



print(numbers)
