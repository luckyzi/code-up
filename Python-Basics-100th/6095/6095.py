# [0,0]으로 구성된 바둑판 생성
d = []
for i in range(20):
  d.append([])
  for j in range(20):
    d[i].append(0)

# 입력을 받아서 x,y값을 구한 뒤 해당 값에 돌이 있다는 1을 할당

n = int(input())
for i in range(n):
  x, y = input().split()
  d[int(x)][int(y)] = 1

# 입력된 바둑판의 값을 출력
for i in range(1, 20):
  for j in range(1, 20):
    print(d[i][j], end=' ')
  print() # 줄바꿈을 위한 코드