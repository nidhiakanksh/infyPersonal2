############CHEAT_SHEAT########################
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
       # self.next2=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def printList(self):
        
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
        
            
    def insertNode(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
    
    def insertMidNode(self,data,prevData):
        newNode=Node(data)
        temp=self.head
        while(temp):
            if temp.data==prevData:
                newNode.next=temp.next
                temp.next=newNode
                break
            
            else:
                temp=temp.next
    def addNode(self,data):
        newNode=Node(data)
        
        if self.head==None:
            self.head=newNode
            return
        temp=self.head
        while(temp):
            if temp.next==None:
                temp.next=newNode
                break
            else:
                temp=temp.next
    
    def deleteNode(self,data):
        temp=self.head
        while(temp and temp.next!=None):
            if(temp.next.data==data):
                temp.next=temp.next.next
                return
            else:
                temp=temp.next
        print('Empty List')
        
    def deleteNodeAt(self,pos):
        
        temp=self.head
        count=0
        prev=None
        while(temp):
            
            if count==pos:
                if count==0:
                   
                   self.head=temp.next
                   break
                else:
                   prev.next=temp.next
                   break
            else:
                prev=temp
                temp=temp.next
                count+=1
                
    def deleteLinkedList(self):
            temp=self.head
            i=0
            while(temp):
                print(i)
                front=temp.next
                del temp.data
                
                temp=front
                i=i+1
    def findLengthIter(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        return count 
    
    #Recursively Calculating the Length of a linkedList starting from a particular node
    def findLengthRec(self,startNode):
        if startNode==None:
            return 0
        else:
            return 1+self.findLengthRec(startNode.next)
       
   #Iteratively searching an elemet in the linked list
    def searchElementIter(self,node):
        temp=self.head
        while temp:
            if temp.data==node:
                return "Yes"
            else:
                temp=temp.next
        return "No"
   
    #Recursively searching for an element in the linked List
    def searchElementRec(self,startNode,node):
        if not startNode:
            return "No"
            
        if startNode.data==node:
            return "Yes"
        else:
            return self.searchElementRec(startNode.next,node)
       
    #Function to get the nth node in a linked list
    def getNthNode(self,n):
        count=0
        temp=self.head
        while temp:
            if count==n:
                return temp.data
            temp=temp.next
            count+=1
        print("n > (length of LinkedList")
        
    #Function to find the nth node from the end of the linkedlist
    def getNthNodeFromEnd(self,n):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        temp=self.head
        for i in range (0,count-n-1):
            temp=temp.next
        return temp.data
    
     #Function to find the middle node from the end of the linkedlist
    def getMidNode(self):
        temp=self.head
        count=0
        while temp:
            count+=1
            temp=temp.next
        temp=self.head
        for i in range (0,count//2):
            temp=temp.next
        return temp.data
    
    
    #Finding Mid by two pointer approach
    def getMidNodeByTwoPointer(self):
        slow=self.head
        fast=self.head
        
        while fast:
            
            fast=fast.next
            if fast:
                fast=fast.next
            else:
                break
            slow=slow.next
        return slow.data
                
    #Function to return the number of occurances of a key (recursively)
    def noOfOccurencesOf(self,startNode,key):
         if not startNode:
               return 0
           
         if startNode.data==key  :
            return 1+ self.noOfOccurencesOf(startNode.next,key)
         else:
            return 0+ self.noOfOccurencesOf(startNode.next,key)
    
    #Function to check if there is 
    def checkLoop(self):
        temp=self.head
        id_list=[]
        while temp:
            
            
         
     
   
    
    
    
    
            
    
if __name__=='__main__':
    # llist=LinkedList()
    # first=Node(1)
    # llist.head=first
    # #print(llist.head.data)
    # second=Node(2)
    # third=Node(3)
    # llist.head.next=second
    # second.next=third
    # llist.insertMidNode(6, 2)
    # llist.addNode(99)
    # llist.printList()
    # llist.deleteNode(1)
    # llist.printList()
    
    
    #DeleteNodeAtIndex
    l2=LinkedList()
    l2.addNode(10)
    l2.addNode(20)
    l2.addNode(30)
    l2.addNode(40)
    l2.addNode(50)
    
    l2.printList()
    
    l2.deleteNodeAt(0)
    
    
    l2.printList()
  #  l2.deleteLinkedList()
    print("Deleting")
    l2.printList()
    
    # Finding the  Length of Linked List (Iterative) :
    print(l2.findLengthIter())
    
    
    #Finding the  Length of Linked List (Recursive) :
    print("Finding the  Length of Linked List (Rec) :")
    l3=LinkedList()
    l3.addNode("Akanksh")
    l3.addNode("Nidhi")
    l3.addNode("Aditya")
    l3.addNode("Ashith")
    l3.addNode("Ash")
    l3.addNode("Ashu")
    l3.addNode("AshDBX")
    l3.printList()
    
    print(l3.findLengthRec(l3.head.next))
    print(l3.searchElementIter("Jaggasa"))
    print(l3.searchElementIter("Ashith"))
    
    print("Finding if the element is present or not (Rec)")
    
    print(l3.searchElementRec(l3.head,"Akanksh"))
    print(l3.searchElementRec(l3.head,"Ash"))
    
    #Function to get the nth Node in a linked List
    print(l3.getNthNode(4))
    
    #Function to find the nth node from the end of the linkedlist
    print(l3.getNthNodeFromEnd(3))
    
    print("BEFORE")
    l3.printList()
    print("Middle:"+l3.getMidNode())
    
    l3.deleteNodeAt(4)
    l3.deleteNodeAt(5)
   
    
    l3.deleteNodeAt(0)
    l3.addNode("Nidhi")
    l3.addNode("Nidhi")
    print("AFTER")
    l3.printList()
    print("Middle:"+l3.getMidNode())
    
    
    #Deleting node using two pointer approach
    print("Middle by 2 pointer: "+ l3.getMidNodeByTwoPointer())

    print("-------------------------------------")
   
    
    # Function to return the number of occurances of a key (recursively)
    print(l3.noOfOccurencesOf(l3.head,"Nidhi"))
    
    
    print("-------------------------------------")
   
    
    l3.printList()
    
    print("-----Checking if the list has a loop or not !------")
    
    loopList=LinkedList()
    first=Node(1)
    loopList.head=first
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
    fifth=Node(5)
    
    #Forming the circular pattern
    first.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth
    fifth.next=second
    
        
    #Printing my Looplist
    # Cant print using this function loopList.printList()
    
    
    #Function Call for checking if the list has a loop or not
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    