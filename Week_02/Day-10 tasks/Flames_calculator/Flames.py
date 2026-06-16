class FlamesCalculator:

    def __init__(self,name1,name2):
        self.__name1=name1
        self.__name2=name2

    def __CountMatching(self):
        list1 = list(self.__name1)
        list2= list(self.__name2)

        for ch in self.__name1:
            if ch in list2:
                list1.remove(ch)
                list2.remove(ch)

        count = len(list1) + len(list2)
        return count
    
    def FlamesFinder(self):
        FLAMES = ("F","L","A","M","E","S")
        while len(FLAMES) >1:
            index = (self.__CountMatching()-1)% len(FLAMES)
            FLAMES= FLAMES[index+1:] + FLAMES[:index]
        result = FLAMES[0]
        return result
    
    def FlamesResult(self):
        result = self.FlamesFinder()
        flames={
            "F": "Friends",
            "L": "Lover",
            "A": "Affection",
            "M": "Marriage",
            "E": "Enemies",
            "S": "Sister"
        }


        print("Flames Result :",flames[result])
        

name1 = input("Enter the Name 1:").lower()
name2 = input("Enter the Name 2:").lower()

flames1=FlamesCalculator(name1,name2)
flames1.FlamesResult()



