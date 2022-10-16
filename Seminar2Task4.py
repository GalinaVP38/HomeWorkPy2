from random import randint

n = int(input("Введите число n: "))
dict = {}
multiply = 1
for i in range(1, n+1):
    dict[i] = randint(-n, n)
print(dict)
i = int(input("Введите позицию первого элемента от 1 до n: "))
j = int(input("Введите позицию второго элемента от 1 до n: "))
if (0<=i<=n) and (0<=j<=n):
    multiply = int(dict[i]*dict[j])
    print(f"Произведение элементов: {multiply}")
else: print("Введены некорректные позиции элементов")
