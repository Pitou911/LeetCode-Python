def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        check = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        N = len(s)
        i = N-1
        while i >= 0:
            if i < N-1 and check[s[i]] < check[s[i+1]]:
                result -= check[s[i]]
            else:    
                result += check[s[i]]
            i -= 1
        return result

print(romanToInt("MXVIIII"))