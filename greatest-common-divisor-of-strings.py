import copy
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        #always check if str2 * x = str1
        ###if it is, return str2 * x
        #str2 = str2 - end character
        #reevaluated x (remainder) (not most efficient but will get the job done)
        #check if str2 * x = str1
        ### if after looping, nothing works, return ""
        str3 = copy.deepcopy(str2)
        if(len(str1)>=len(str2)):
            while(len(str2) != 0):
                multiplier = int(len(str1)/len(str2))
                if((str2 * multiplier == str1) and (len(str3)%len(str2) == 0)):
                    multiplier2 = len(str3)/len(str2)
                    if(multiplier2 * str2 == str3):
                        return str2
                str2 = list(str2)[:-1]
                str2 = "".join(str2)
                print("str2")
                print(str2)
                print("str3")
                print(str3)
            return ""
        str3 = copy.deepcopy(str1)
        while(len(str1) != 0):
            
            multiplier = int(len(str2)/len(str1))
            if((str1 * multiplier == str2) and (len(str3)%len(str1) == 0)):
                multiplier2 = len(str3)/len(str1)
                if(multiplier2 * str1 == str3):
                    return str1
            str1 = list(str1)[:-1]
            str1 = "".join(str1)
            print("str1")
            print(str1)
            print("str3")
            print(str3)
        return ""
