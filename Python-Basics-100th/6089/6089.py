num1, num2, num3 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

for i in range(1, num3):
  num1 *= num2

print(num1)