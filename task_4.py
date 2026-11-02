text = input("Введите строку: ")

text = text.lower()
text = text.replace(" ","")

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

if text == reversed_text:
    print("Строка является палиндромом")
else:
    print("Cтрока не является палиндромом")