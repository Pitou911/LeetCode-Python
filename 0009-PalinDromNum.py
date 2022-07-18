def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        for i in range(len(string)):
            if string[i] != string[len(string)-i-1]:
                return False
        return True

if isPalindrome(1213):
    print("It is Palindrome Number")
else:
    print("It is not Palindrome Number")