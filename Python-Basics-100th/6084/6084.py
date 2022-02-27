num1, num2, num3, num4 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

result = round(num1 * num2 * num3 * num4 /8 / 1024 / 1024, 1)
print(result, 'MB')