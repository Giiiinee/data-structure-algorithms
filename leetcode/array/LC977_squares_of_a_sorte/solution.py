#有序数组的平方
class Solution(object):
    def sortedSquares(self, nums):
        k=len(nums)-1
        i=0
        j=len(nums)-1
        res=[0]*len(nums)
        while i<=j:
            if (nums[i])**2>(nums[j])**2:
                res[k]=(nums[i])**2
                k-=1
                i+=1
            else:
                res[k]=(nums[j])**2
                k-=1
                j-=1
        return res
