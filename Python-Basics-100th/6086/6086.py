num = int(input())
sum = 0
count = 1
while True:
  sum += count
  count += 1
  if sum >= num:
    break;

print(sum)
