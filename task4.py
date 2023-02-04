print("Введите ширину шоколадки")
n = int(input())
print("Введите длинну шоколадки")
m = int(input())
print("Введите количество долек")
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('YES')
else:
    print('NO')