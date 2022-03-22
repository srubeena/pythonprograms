#Program to print Right Half Pyramid
num_rows = int(input("Enter the number of rows"));
sp= int(num_rows/2)
k=8
for i in range(0, sp+1):
    for j in range(0, k):
        print(end=" ")

    k = k - 2
    for j in range(0, i+1):
        print("* ", end="")
    print()