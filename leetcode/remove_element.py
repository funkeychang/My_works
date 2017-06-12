class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)

        return len(nums)

        """ Faster solution(42ms)
        begin = 0

        for index, num in enumerate(nums):
            if num != val:
                nums[begin] = num
                begin+=1

        return begin
        """
