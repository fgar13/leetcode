class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = []
        if "*" not in s:
            return s
        for count, val in enumerate(s):
            if val != "*":
                ans.append(s[count])
            if val == "*":
                if(len(ans) != 0):
                    ans.pop(len(ans) - 1)
        return "".join(ans)