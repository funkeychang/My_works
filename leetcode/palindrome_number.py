class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        rx = str(x[::-1])
        return True if rx == x else False

        """ faster
        s = str(x)
        return s == s[::-1]
        """
