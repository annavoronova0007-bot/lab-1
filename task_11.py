age = int(input("Введите ваш возраст: "))
income = float(input("Введите ваш ежемесячный доход: "))
loan_amount = float(input("Введите размер запрашиваемого кредита: "))
term = int(input("Введите срок кредита(месяцы): "))
history = input("Какая у вас кредитная история?(отличная/хорошая/удовлетворительная/плохая)")
guarantor = input("Есть ли у вас поручитель(да/нет): ")
deposit = input("Есть ли у вас залог(да/нет): ")

ratio = loan_amount/(income*term)

if age>63 or age<18 or history=="плохая" or ratio > 0.5:
    risk = "Критический"
    percentage = 0.30
    answer = "Отказано"
elif history == "удовлетворительная" and guarantor == "нет" and deposit == "нет":
    risk = "Высокий"
    percentage = 0.20
    answer = "Отказано"
elif ratio > 0.3:
    risk = "Средний"
    percentage = 0.15
    answer = "Одобрено" 
else:
    risk = "Низкий"
    percentage = 0.10
    answer = "Одобрено"

print ("Соотношение кредита к доходу:",round(ratio,3))
print ("Категория риска:",risk)
print ("Предложенная процентная ставка:",percentage)
print ("Статус кредита: ",answer)



