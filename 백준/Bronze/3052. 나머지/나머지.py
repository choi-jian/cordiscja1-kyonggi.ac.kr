n=[]
for i in range(10):
  s=int(input())
  x=s%42
  n.append(x)

y=set(n)
print(len(y))