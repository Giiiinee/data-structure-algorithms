#反转链表

#法一(双指针)
class Solution(object):
    def reverseList(self, head):
        cur=head
        pre=None
        while cur!=None:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre

  #法二(递归)
  class Solution(object):
    def reverseList(self,head):
        return self.reverse(head,None)
    def reverse (self,cur,pre):
        if cur == None:
            return pre
        temp=cur.next
        cur.next=pre
        return self.reverse(temp,cur)
