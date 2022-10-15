n = int(input("Введите число n:"))
dict = {}
sum = 0
for i in range(1, n+1):
    dict[i] = round((1+1/i)**i, 2)
    sum+=float(dict[i])
print(f"Список: {dict}")
print(f"Сумма чисел: {sum}")
