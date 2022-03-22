import itertools
from typing import List


class StringClass:

    def __init__(self, string):
        self.str = string

    def lengthOfString(self):
        strlen= len(self.str)



    def convertStringToList(self):
        #lis=List(string)
        print(list(self.str))
        return list(self.str)

#objstr=StringClass('12345')
#objstr.convertStringToList()




class PairsPossible(StringClass):

    def __init__(self, string):
        self.str = string
        self.lst = StringClass.convertStringToList(self)
        #self.str = string
    # print(StringClass.convertStringToList(self))
    #self.lst = StringClass.convertStringToList(lst)

    def possiblepairs(self):
        index1=0
        index2=1
        #listlen=StringClass.lengthOfString(self)
        pairs = []

        #lst = StringClass.convertStringToList(self.str)
        print(self.lst)
        #lst=StringClass.convertStringToList(self)
        for element1 in self.lst[index1:]:
            for element2 in self.lst[index2:]:
               pairs.append((element1, element2))
               index2 += 1

            index1 += 1
            index2 = 0
        return pairs


    def getpairs(self):
        print(self.possiblepairs())



objstr=StringClass('12345')
obj2=objstr.convertStringToList()
objpair=PairsPossible('654321')
objpair.getpairs()
#objpair.convertStringToList()
#print(objpair.possiblepairs())
#objpair=PairsPossible(objstr.convertStringToList())



