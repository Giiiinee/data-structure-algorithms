#两个数组的交集
class Solution(object):
    def intersection(self, nums1, nums2):
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        return list(res)
