#有效的字母异位词
##哈希表法
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        count=[0]*26
        for i in s:
            count[ord(i)-ord('a')]+=1
        for i in t:
            count[ord(i)-ord('a')]-=1
        for nums in count:
            if nums!=0:
                return False
        return True
##排序法
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        sorted_s=sorted(s)
        sorted_t=sorted(t)
        return sorted_s==sorted_t
##Counter法
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s)==Counter(t)
