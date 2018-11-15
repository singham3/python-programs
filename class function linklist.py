#wap to creat single linklist
class Node:
    def __init__(self):
        self.data=None
        self.next=None
class linkedlist:
    def __init__(self,head=None):
        self.head=head
    def create(self):
        while True:
            NewNode=Node()
            NewNode.data=int(input("enter data part: "))
            if self.head==None:
                self.head=NewNode
                current=NewNode
            else:
                current.Next=NewNode
                current=NewNode
            c=input("do you want")
    def PrintNode(self):
        curr=self.head
        while curr:
            ptint(curr.data)
            curr=curr.Next
    def InsertionatLast(self):
        NewNode=Node()
        NewNode.data=int(input("Enter data part: "))
        ptr=self.head
        while ptr.Next!=None:
            ptr=ptr.Next
        ptr.next=NewNode
    def deletionatLast(self):
        ptr=self.head
        while ptr.Next!=None:
            pre=ptr
            ptr=ptr.Next
        pre.Next=None
        del ptr

MyList=linkedlist()
MyList.create()

print("printing")
MyList.PrintNode()
#MyList.printReverse (MYList.head)
#MyList.InsertionatList()
MyList.DeletionaList()
MyList.PrintNode()
