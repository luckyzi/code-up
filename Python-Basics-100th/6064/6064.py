num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

print((num1 if (num1 <= num2) else num2) if (num2 < num3) else num3)
