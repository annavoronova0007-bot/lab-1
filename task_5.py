firstNum = float(input("Введите первое число: "))
secondNum = float(input("Введите второе число: "))

math_operation = input("Введите математическое действие(+ - / * ^ %): ")

if math_operation == "+":
    print("Сумма", firstNum, "+" , secondNum, "=", firstNum+secondNum)
elif math_operation == "-":
    print("Разность", firstNum, "-" , secondNum, "=", firstNum-secondNum)
elif math_operation == "*":
    print("Произведение", firstNum, "*" , secondNum, "=", firstNum*secondNum)
elif math_operation == "^":
    print(firstNum, "^" , secondNum, "=", firstNum**secondNum)
elif math_operation == "%":
     if secondNum==0:
            print("Деление на 0 нельзя")
     else:
            print("Остаток от деления", firstNum, "на" , secondNum, "=", firstNum%secondNum)
elif math_operation == "/":
    if secondNum==0:
        print("Деление на 0 нельзя")
    else:
        print("Частное", firstNum, "/" , secondNum, "=", firstNum/secondNum)
else:
    print("Неверно введен знак математической операции")