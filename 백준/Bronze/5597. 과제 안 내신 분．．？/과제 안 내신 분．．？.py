student=[i for i in range(1,31)]
for s in range(28):
  s=int(input())
  student.remove(s)
print(min(student))
print(max(student))