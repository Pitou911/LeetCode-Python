def divide(dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX = 2147483647
        MIN = -2147483648
        d = abs(dividend)
        dv = abs(divisor)
        result = 0
        while d>=dv:
            temp = dv
            mul = 1
            while d >= temp:
                d -= temp
                result+= mul
                mul += mul
                temp += temp
        if (dividend < 0 and divisor >= 0) or (divisor < 0 and dividend>=0):
            result = -result
        return min(2147483647, max(-2147483648,result))

print(divide(100,20))