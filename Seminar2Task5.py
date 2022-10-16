from random import randint

list = [159 , 152 , 140 , 128 , 113]
temp = 0
n=randint(0, 3)
for i in range(n, 4):
    temp = list[i]
    list[i]=list[i+1]
    list[i+1]=temp
print(n)
print(list)
