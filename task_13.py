text = input("Введите числа:")
str_numbers = text.split()

numbers = []
for num in str_numbers:
    if "." in num:
        numbers.append(float(num))
    else:
        numbers.append(int(num))

repetitions = {}
for num in numbers:
    if num in repetitions:
        repetitions[num] += 1
    else:
        repetitions[num] = 1

unique_num = []
repetitions_num = []

for num in repetitions:
    if repetitions[num] == 1:
        unique_num.append(num)
    else:
        repetitions_num.append(num)

chet = []
nchet = []

for num in numbers:
    if num%2 == 0:
        chet.append(num)
    else:
        nchet.append(num)

pol = []
otr = []

for num in numbers:
    if num<0:
        otr.append(num)
    elif num>0:
        pol.append(num)

with_toch = []

for num in numbers:
    if num%1 != 0:
        with_toch.append(num)

sum_five = 0
kr_five = []

for num in numbers:
    if num%5 == 0:
        sum_five += num

max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num>max_num:
        max_num = num
    if num<min_num:
        min_num = num

print ("Уникальный числа:",unique_num)
print ("Повторяющиеся числа:",repetitions_num)
print ("Нечетные числа:",nchet)
print ("Четные числа:",chet)
print ("Положительные числа:",pol)
print ("Отрицательные числа:",otr)
print ("Числа с плавающей точкой:",with_toch)
print ("Сумма чисел, кратных 5:",sum_five)
print ("Максимальное число:",max_num)
print ("Минимальное число:",min_num)



    
