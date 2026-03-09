import threading

user = input("zadaj cisla oddelene medzerou: ")
numbers = list(map(int, user.split()))

def find_max():
    maximum = max(numbers)
    print("najvyssie cislo: ", maximum)

def find_min():
    minimum = min(numbers)
    print("najnizsie cislo: ", minimum)


thread1 = threading.Thread(target=find_max)
thread2 = threading.Thread(target=find_min)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

# test1 = find_max()
# test2 = find_min()
# print(numbers)
