class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        same = []
        for ele in nums1:
            if ele not in same:
                same.append(ele)
        for ele in nums2:
            if ele not in same:
                same.append(ele)
        answer = []
        a1 = []
        for ele in same:
            if ele not in nums2:
                a1.append(ele)
        answer.append(a1)
        a2 = []
        for ele in same:
            if ele not in nums1:
                a2.append(ele)
        answer.append(a2)
        return answer