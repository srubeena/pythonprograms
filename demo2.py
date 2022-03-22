n = int(input("Enter row count: "))


#space=n
#spac= int((n-1)/2)
first=int(n/2+1)
second=int(first-1)
for i in range(first):
    print(' '*(first-i-1) + ("*")*(2*i+1))

for j in range(second):
    print(' '*(j+1) + ("*")*(n-2))
    n -=2
