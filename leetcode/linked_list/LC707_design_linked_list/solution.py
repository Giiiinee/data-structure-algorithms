#LC707设计链表
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
class MyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
        
    def get(self,index):
        if index<0 or index>=self.size:
            return -1
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr.val
    
    def addAtHead(self,val):
        dummy_head=ListNode(val)
        dummy_head.next=self.head
        self.head=dummy_head
        dummy_head.val=val
        self.size+=1
    
    def addAtTail(self,val):
        new_node=ListNode(val)
        if self.head is None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=new_node
        self.size+=1

    def addAtIndex(self,index,val):
        if index > self.size:
            return
        if index==0:
            self.addAtHead(val)
            return
        curr=self.head
        for _ in range(index-1):
            curr=curr.next
        new_node=ListNode(val)
        new_node.next=curr.next
        curr.next=new_node
        self.size+=1

    def deleteAtIndex(self,index):
        if index<0:
            return
        curr=self.head
        if index==0:
            if self.head!=None:
                self.head=self.head.next
                self.size-=1
            return
        for _ in range(index-1):
            if curr is None:
                return
            curr=curr.next
        if curr is None or curr.next is None:
            return
        curr.next=curr.next.next
        self.size-=1
