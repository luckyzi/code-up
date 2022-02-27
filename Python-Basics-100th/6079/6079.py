풀이1

num = int(input())
sum = 0
count = 0

for i in range(1, num):
    sum += i
    if num <= sum:
        count = i
        break;

print(count)


풀이2

num = int(input())
sum = 0
count = 0

while num >= sum:
    count += 1
    sum += count
    if num <= sum:
        print(count)
        break;
    