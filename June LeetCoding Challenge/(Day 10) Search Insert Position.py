class Solution(object):
    def searchInsert(self, nums, target):
        m=nums.count(target)
        flag=0
        n=0
        if m!=0:
            return nums.index(target)
        else:
            for i in nums:
                if(i>target):
                    flag=1;
                    n=i
                    break;
            if flag==1:
                return nums.index(n)
            else:
                return len(nums)
                     
