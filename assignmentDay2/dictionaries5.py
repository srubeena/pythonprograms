
#def Merge(dict1, dict2):
 #   return (dict2.update(dict1))


# Driver code
#dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# This return None
#print(Merge(dict1, dict2))

# changes made in dict2
#print(dict2)


def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


# Driver code
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = Merge(dict1, dict2)
print(dict3)