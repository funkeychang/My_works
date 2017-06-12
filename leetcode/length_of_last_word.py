class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(' ')[-1])

        """ Better solution
        list_words = s.split()

        if len(list_words) > 0:
            return len(list_words[-1])
        else:
            return 0
        """
