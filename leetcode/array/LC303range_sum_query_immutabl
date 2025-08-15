#区域和检索
class NumArray(object):
    def __init__(self, nums):
        self.pre=[0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            self.pre[i]=self.pre[i-1]+nums[i-1]
    def sumRange(self, left, right):
        return self.pre[right+1]-self.pre[left]
