from python_Oops.assignment1 import PairsPossible


class SearchCommonElements(PairsPossible):

    dict = {}

    def __init__(self,string1,string2):
        self.dict[0]=string1
        self.dict[1]=string2


    def commonElements(self):

        print(self.dict)



comm = SearchCommonElements('12345','476612')
comm.commonElements()