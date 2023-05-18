class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        stringToReturnArr = []
        word1len = len(word1)
        word1Arr = list(word1)
        word2len = len(word2)
        word2Arr = list(word2)
        if(word1len >= word2len):
            for i in range(word2len):
                stringToReturnArr.append(word1Arr[i])
                stringToReturnArr.append(word2Arr[i])
            for i in range(word2len, word1len):
                stringToReturnArr.append(word1Arr[i])
            returnVal = "".join(stringToReturnArr)


        if(word1len < word2len):
            for i in range(word1len):
                stringToReturnArr.append(word1Arr[i])
                stringToReturnArr.append(word2Arr[i])
            for i in range(word1len, word2len):
                stringToReturnArr.append(word2Arr[i])
            returnVal = "".join(stringToReturnArr)


        return returnVal