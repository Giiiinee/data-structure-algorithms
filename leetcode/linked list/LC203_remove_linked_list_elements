#移除链表元素
class Solution(object):
    def removeElements(self, head, val):
        dummy_head=ListNode(next=head)
        current=dummy_head
        while current.next:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        return dummy_head.next
