num1 = int(input())
num2 = input().split()

while len(num2) >= 2:
  if int(num2[0]) > int(num2[1]) :
    del num2[0]
  else:
    del num2[1]
print(num2[0])

모범답안

n = int(input())
a = input().split()

for i in range(n) :
  a[i] = int(a[i])

min = a[0]
for i in range(0, n) :
  if a[i] < min :
    min = a[i]

print(min)