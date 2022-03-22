list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

#list3=list1 + list2
a=len(list1)
b=len(list2)
lis=[]
for x in range(a):
    for y in range(b):
        #str=list1[x] + list2[y]
        lis.append(list1[x] + list2[y])
        #lis +=[str]

print(lis)
        #print("{} {}".format(list1[x],list2[y]))