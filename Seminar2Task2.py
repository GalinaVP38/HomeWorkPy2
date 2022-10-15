n=int(input("Введите число n:"))
def funct(b):
    count = 1
    for i in range(1, b+1):
        print(count, end = ', ')
        count*=(i+1)
funct(n)
