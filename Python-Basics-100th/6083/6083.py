num1, num2, num3 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
sum = 0

for i in range(0, num1):
    for j in range(0, num2):
        for k in range(0, num3):
            print(i, j, k)
            sum += 1
print(sum)