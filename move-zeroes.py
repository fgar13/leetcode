#This is not my own solution
#I liked this solution more than my own
#My solution essentially amounted to a sorting algorithm
#Due to the constraints not being clear enough
#i.e. The constraints did not make mention...
#Of the fact that the elements of the array...
#Were already in ascending order
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for j in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)