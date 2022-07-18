class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        else:
            try:
                index = haystack.index(needle)
                return index
            except ValueError:
                return -1