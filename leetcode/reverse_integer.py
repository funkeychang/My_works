class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        s = str(abs(x))
        rs = int(s[::-1])

        if rs > 2 ** 31:
            return 0

        if x >= 0:
            return int(s[::-1])
        else:
            return int('-'+s[::-1])
