num=[] #num 이라는 배열을 만들고 시작 
for i in range(10):
  n=int(input())%42
  if n not in num:
    num.append(n)

print(len(num))