#LC142环形链表II
class Solution(object):
    def detectCycle(self, head):
        fast=head
        slow=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                index1=fast
                index2=head
                while index1 != index2:
                    index1=index1.next
                    index2=index2.next
                return index1
        return None
