from re import X


def mySqrt(x):

    if x == 0 or x == 1:
        return x
    start = 1
    end = x
    while start <= end:
        mid = (start + end) // 2
        mid_s = mid * mid
        if mid_s == x:
            return mid
        if mid_s < x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans

print(f"The square root of 83 is {mySqrt(83)}")