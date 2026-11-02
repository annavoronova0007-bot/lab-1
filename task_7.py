minutes = float(input("Введите количество израсходованных минут за месяц(мин):"))
sms = float(input("Введите количество израсходованных смс-сообщений за месяц:"))
internet = float(input("Введите количество израсходованного интернет трафика за месяц(мб):"))

sum = 24.99

if minutes > 60:
    addMin = minutes - 60
    sumM = addMin*0.89
    sum = sum + sumM
    print("Минут вне трафика:", addMin)
    print("Начисление за минуты:", round(sumM,2))
if sms > 30:
    addSms = sms - 30
    sumS = addSms*0.59
    sum = sum + sumS
    print("Cмс вне трафика:", addSms)
    print("Начисление за cмс:", round(sumS,2))
if internet > 1024:
    addInt = internet - 1024
    sumInt = addInt*0.79
    sum = sum + sumInt
    print("Интернета вне трафика(Мб):", addInt)
    print("Начисление за интернет:", round(sumInt,2))

sum = 1.02*sum

print("Базовая сумма тарифа: 24.99")
print("Итоговая сумма к оплате:",round(sum,2))







