s = input("Введите число: ")
sum = 0

for i in range(len(s)):
    if s[i]=="." or s[i]=="-":
        sum=sum
    else:
        sum=sum+int(s[i])
print(f"Сумма цифр в вашем числе: {sum}")
