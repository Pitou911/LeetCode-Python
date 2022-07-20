def num_ways_bottom_up(n):
        if n == 0 or n == 1: return 1
        nums = [None]*(n+1)
        nums[0] = 1
        nums[1] = 1
        for i in range(2, n+1):
            nums[i] = nums[i-1] + nums[i-2]
        return nums[n]
            
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    return num_ways_bottom_up(n)

print(f"The number of method you can climb the stair of 6 is {climbStairs(6)}")