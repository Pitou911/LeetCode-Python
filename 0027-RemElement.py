class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                #partition(qsort)
                nums[k] = nums[i]
                k += 1
        return k