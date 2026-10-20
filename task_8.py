import random
num = random.randint(1,100)

print("Я загадал число от 1 до 100, угадай!")

while True:
    myNum = int(input("Твое число: "))
    if myNum > num:
        print("Меньше")
    elif myNum < num:
        print("Больше")
    else:
        print("Ты угадал!")
        break
