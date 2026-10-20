units = {
    "мм": 0.001,
    "см": 0.01,
    "дм": 0.1,
    "м": 1.0,
    "км": 1000.0,
    "дюйм": 0.0254,
    "фут": 0.3048,
    "ярд": 0.9144,
    "миля": 1609.34,
    "морская миля": 1852.0
}

print("Доступные единицы измерения:", list(units.keys()))

from_unit = input("Из какой единицы переводим? ")
to_unit = input("В какую единицу переводим? ")
value = float(input("Введите значение: "))

result = value * units[from_unit] / units[to_unit]

print(value, from_unit, "=", result, to_unit)