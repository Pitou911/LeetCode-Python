def permute(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        #base case
        if(len(nums) == 1):
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = permute(nums)
            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

nums = [1,2,3]
print(permute(nums))