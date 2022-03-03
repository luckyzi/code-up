num1, num2, num3 = input().split()

num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
day = 1

while day % num1 != 0 or day % num2 != 0 or day % num3 != 0 :
  day +=1

print(day)