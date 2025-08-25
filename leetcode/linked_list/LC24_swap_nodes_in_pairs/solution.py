#两两交换链表中的节点
class Listnode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution(object):
    def swapPairs(self, head):
        dummy_head=Listnode()
        dummy_head.next=head
        cur=dummy_head
        while cur.next!=None and cur.next.next!=None:
            temp=cur.next
            temp1=cur.next.next.next
            cur.next=cur.next.next
            cur.next.next=temp
            temp.next=temp1
            cur=cur.next.next
        return dummy_head.next
