num1, num2, num3 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

result = round(num1 * num2 * num3 /8 / 1024 / 1024, 2)
print('%.2f'%result, 'MB')
