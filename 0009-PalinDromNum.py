#convert int to string
# def isPalindrome(x):
#         """
#         :type x: int
#         :rtype: bool
#         """
#         string = str(x)
#         for i in range(len(string)):
#             if string[i] != string[len(string)-i-1]:
#                 return False
#         return True

#second method:
def isPalindrome(x):
    if x < 0:
        return False
    div = 1
    while x >= div * 10:
        div = div * 10
    while x:
        left = x % 10
        right = x // div
        if left != right:
            return False
        else:
            x = (x % div)//10
            div /= 100
    return True

if isPalindrome(1213121):
    print("It is Palindrome Number")
else:
    print("It is not Palindrome Number")