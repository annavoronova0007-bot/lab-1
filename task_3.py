sum = int(input("Введите сумму в рублях: "))

one_h = sum//100
remainder = sum%100

fifty = remainder//50
remainder = remainder%50

ten = remainder//10
remainder = remainder%10

five = remainder//5
remainder = remainder%5

two = remainder//2
remainder = remainder%2

one = remainder

print("Купюр 100 рублей:", one_h)
print("Купюр 50 рублей:", fifty)
print("Купюр 10 рублей:", ten)
print("Купюр 5 рублей:", five)
print("Купюр 2 рублей:", two)
print("Купюр 1 рублей:", one)








