num1 = int(input())
num2 = input().split()

for i in range(num1):
  num2[i] = int(num2[i])

result = []
for i in range(24):
  result.append(0)

for i in range(num1):
  result[num2[i]] += 1

for i in range(1, 24):
  print(result[i], end=' ')