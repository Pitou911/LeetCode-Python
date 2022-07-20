def plusOne(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ""
        #convert ele to string
        for i in digits:
            string += str(i)
        string = int(string)
        string += 1
        string = str(string)
        res = []
        for j in range(len(string)):
            res.append(int(string[j]))
        return res
print(f"Before: [1, 2, 3]")
print(f"After: {plusOne([1,2,3])}")