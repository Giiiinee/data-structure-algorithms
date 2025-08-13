#长度最小的子数组
class Solution(object):
    def minSubArrayLen(self, target, nums):
        i=0
        sum=0
        result=float('inf')
        for j in range(len(nums)):
            sum += nums[j]
            while(sum>=target):
                s=j-i+1
                result=min(result,s)
                sum=sum-nums[i]
                i+=1
        if result==float('inf'):
            return 0
        else:
            return result
