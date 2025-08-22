#LC707设计链表

#法一单链表做法(类方法之间的调用不要求严格顺序)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val   #给节点的值val提供一个默认值
        self.next = next    #给节点的后继指针next提供默认值

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  #虚拟头结点

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index + 1):  #多走一步到真正节点
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)    #调用之后的addAtIndex函数

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index,val):
        if index > self.size:
            return      #当函数遇到无法继续执行合理逻辑的情况时，用空return快速终止函数，不返回具体内容
        if index < 0:
            index = 0
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next

#法一双链表做法
class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
        self.prev=None

class MyLinkedList:
    def __init__(self):
        self.dummy_head = Node(0)
        self.dummy_tail = Node(0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0
    
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        if index < self.size - index:
            curr = self.dummy_head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.dummy_tail.prev
            for _ in range(self.size -1 - index):
                curr = curr.prev
        return curr.val

    def addAtIndex(self,index,val):
        if index>self.size:
            return
        if index<0:
            index=0
        pred,succ=self.dummy_head,self.dummy_head.next
        for _ in range(index):
            pred=pred.next
            succ=succ.next
        to_add=Node(val)
        to_add.prev=pred
        to_add.next=succ
        pred.next=to_add
        succ.prev=to_add
        self.size+=1

    def deleteAtIndex(self,index):
        if index<0 or index>=self.size: 
            return
        pred=self.dummy_head
        for _ in range(index):
            pred=pred.next
        succ=pred.next
        pred.next=succ.next
        succ.next.prev=pred
        self.size-=1

    def addAtHead(self,val):
        self.addAtIndex(0,val)

    def addAtTail(self,val):
        self.addAtIndex(self.size,val)


#法二单链表做法
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    
class MyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
        
    def get(self,index):
        if index<0 or index>=self.size:    #长度为3的链表索引为0，1，2
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
