"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""



def my_func1(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[len(numbers) - 2] + numbers[len(numbers) - 1]

def my_func2(a, b, c):
    if a >= b and a >= c:
        max_val = a
        if b >= c:
            return a + b
        else:
            return a + c
    elif b >= a and b >= c:
        max_val = b
        if a >= c:
            return b + a
        else:
            return b + c
    else:
        max_val = c
        if a >= b:
            return c + a
        else:
            return c + b

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

result1 = my_func1(a, b, c)
result2 = my_func2(a, b, c)
print(result1)
print(result2)
