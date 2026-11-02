text1 = input("Введите первый набор чисел:")
text2 = input("Введите второй набор чисел:")

s_numbers1 = text1.split()
s_numbers2 = text2.split()

numbers1 = []
numbers2 = []
for num in s_numbers1:
    if "." in num:
       numbers1.append(float(num))
    else:
        numbers1.append(int(num))

for num in s_numbers2:
    if "." in num:
        numbers2.append(float(num))
    else:
        numbers2.append(int(num))

povtor = []
npovtor1 = []
npovtor2 = []
for num1 in numbers1:
    for num2 in numbers2:
        if num1 == num2:
            povtor.append(num1)

for num in numbers1:
    if num not in povtor:
        npovtor1.append(num)

for num in numbers2:
    if num not in povtor:
        npovtor2.append(num)
    
print("Повторяющиеся числа:",povtor)
print("Числа из первого набора, которых нет во втором:",npovtor1)
print("Числа из второго набора, которых нет во втором:",npovtor2)
print("Числа из обоих наборов без пересечений:",npovtor1+npovtor2)







