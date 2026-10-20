sum = float(input("Введите сумму покупок: "))
age =int(input("Введите ваш возраст: "))
birthday = input("Сегодня ваш день рождения?(да/нет): ")
vip = input("Являетесь ли вы вип клиентом?(да/нет): ")

discount = 0

if (vip=="да" or vip=="Да"):
    discount = 15
else:
    if age>=63:
        discount += 5
    if (birthday=="да" or birthday=="Да"):
        discount += 5
    if sum>1000:
        discount += 10

if discount > 25:
    discount = 25

final = sum - discount*sum/100

print("Ваша финальная скидка:",discount)
print ("Итоговая сумма к оплате:",final)