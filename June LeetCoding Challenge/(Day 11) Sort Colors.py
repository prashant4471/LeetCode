class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=nums.count(0)
        b=nums.count(1)
        c=nums.count(2)
        nums.clear()
        for i in range(a):
            nums.append(0)
        for i in range(b):
            nums.append(1)
        for i in range(c):
            nums.append(2)
