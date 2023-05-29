S = input()

aList = [chr(i) for i in range(ord('a'),ord('z')+1)]

for i in range(26):
  a = S.find(aList[i])
  aList[i] = a

for i in range(26):
  print(aList[i],end = " ")