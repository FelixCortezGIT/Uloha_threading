import threading

user = input("zadaj cisla oddelene medzerou: ")
numbers = list(map(int, user.split()))

print(numbers)
