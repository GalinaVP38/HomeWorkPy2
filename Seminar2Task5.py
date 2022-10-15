list = [159 , 152 , 140 , 128 , 113]
temp = 0
for i in range(3):
    temp = list[i]
    list[i]=list[i+1]
    list[i+1]=temp
print(list)
