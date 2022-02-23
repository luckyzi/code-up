num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

print(bool(num1) != bool(num2))

모범답안

num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

print((num1 and (not num2)) or not num1 and num2)
