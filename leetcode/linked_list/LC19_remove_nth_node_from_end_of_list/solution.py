#LC19删除链表的倒数第n个结点
class ListNode():
    def __init__(self,val,next):
        self.val=val
        self.next=next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy_head=ListNode(0,head)
        fast=dummy_head
        slow=dummy_head
        for _ in range(n+1):
            fast=fast.next
        while fast!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy_head.next
