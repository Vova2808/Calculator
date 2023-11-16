
num1 = float(input("Введите первое число: "))
operator = input("Выберите оператор (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
else:
    result = "Ошибка: неправильный оператор"

print("Результат:", result)