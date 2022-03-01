num1, num2, num3, num4 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

for i in range(1, num4):
  num1 = (num1 * num2) + num3

print(num1)