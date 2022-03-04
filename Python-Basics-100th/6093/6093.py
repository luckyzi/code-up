num1 = int(input())
num2 = input().split()

for i in range(num1):
  num2[i] = int(num2[i])

result = []

for i in range(num1 - 1, -1, -1):
  result.append(num2[i])

for i in range(0, num1):
  print(result[i], end=' ')