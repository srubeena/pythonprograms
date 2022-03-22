#Q3 filter
from functools import reduce

lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]
lis=[]

#def remnoveNegative(x):
 #       if x < 0:
  ##         return res

#lis=filter(remnoveNegative,[-1000, 500, -600, 700, 5000, -90000, -17500])




#04
lst2=[-1000, 500, -600, 700, 5000, -90000, -17500]

print(list(filter(lambda a: a >0,(map(lambda a:a*-1,lst2)))))



#05
lis = [1, 3, 5, 6, 2]
print("The answer will be : ", end="")
print(reduce(lambda a, b: a*b, lis))

#6
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
dictionary = dict(zip(lst1, lst2))
print(dictionary)

