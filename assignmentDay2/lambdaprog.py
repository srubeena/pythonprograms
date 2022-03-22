#a=int(input("vlues of a:"))
#b=int(input("b:"))
#c=int(input("c:"))
#x=int(input("x:"))
from itertools import count

res=lambda a,b,c,x: print((a*x**2)+(b*x)+c)
res(2, 3, 1, 2)



lst1=["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]

#seq1 = lambda x: count('A')
#eq2 = lambda x:print(x, count('a'))
#res= filter(seq1,lst1)
#result=list(res)

def countOfchar():
    sum = 0
    sum2 = 0
    for x in lst1:
        res=x.count('A')
        res2=x.count('a')
        sum=sum+res
        sum2=sum2+res2
        #res=count('A')
    print("count of A :", sum)
    print("count of a:", sum2)

countOfchar()

charA=list(map(lambda x: x.count('A'), lst1))
chara=list(map(lambda x: x.count('a'), lst1))
print("count of 'A' in each string/word seq:", charA)
print("count of 'a' in each word ", chara)

#print(sum(charA))
#print(sum(chara))
#lis=map(countOfchar, lst1)
#print(lis)
