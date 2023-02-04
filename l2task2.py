print("Введите сумму чисел")
s = int(input())
print("Введите произведение чисел")
p = int(input())
a = s/2
b = (s + int((s ** 2 - 4 * p) ** 0.5)) // 2
print(a, b)