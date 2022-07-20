# using bruteForce O(n^2)
# def twoSum(nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i in range(len(nums)-1):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]
#         return []

# using hashmap aka Dictionary O(n)
def twoSum(nums, target):
    lookUp = {}
    res = []
    for i in range(len(nums)):
        complement = target - nums[i]
        if lookUp.has_key(complement):
            res.append(lookUp[complement])
            res.append(i)
            break
        else:
            lookUp[nums[i]] = i
    return res

print(twoSum([3,2,3], 6))