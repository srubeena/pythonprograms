#The original dictionary is : {‘HuEx: [1, 3, 4], ‘is’: [7, 6], ‘best’: [4, 5]}
#The converted list is : [[‘HuEx, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]

dict={'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
diclen= len(dict)
lst=[]

#print(dict.items())
    #lst=lst.append(list(dict[items]))

for item in dict:
    #(item,dict[item])
    #lst= lst.append(item)
    #lst= lst[i].append(dict[item])

    lst=("{} ,{}".format(item, dict[item]))
    print(lst)
    lis=[]
    lis=list(map(item, dict[item]))
    print(lis)




