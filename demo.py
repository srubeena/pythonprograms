num = int(input("Enter the number: "))
list1 = [] #an empty list
for i in range(num):
  list1.append([])
  list1[i].append(1)
  for j in range(1, i):
    list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
  if(num != 0):
    list1[i].append(1)
for i in range(num):

  for j in range(0, i + 1):
    print('{0:1}'.format(list1[i][j]), end = " ", sep = " ")
  print("0 " * (num - i -1), end=" ", sep=" ")
  print()