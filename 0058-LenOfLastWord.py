def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        i, length = len(s)-1, 0
        while s[i] == " ":
            i-=1
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1
        return length

word = "The Owrld is Full OF People    "
print(f"The length of the last word is {lengthOfLastWord(word)}")