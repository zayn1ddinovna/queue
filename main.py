import random

print("GUESS THE NUMBER")

a = int(input("Qaysi sondan boshlansin : "))
b = int(input("Qaysi songacha bo'lsin : "))

num = random.randrange(a,b+1)



while True:
    son = int(input("Sonni toping!: "))

    if son > num :
        print("Baland")

    elif son < num :
        print("Past")

    elif son == num:
        print("To'g'ri javob ")
        break
