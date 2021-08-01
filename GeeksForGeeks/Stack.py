
# -*- coding: utf-8 -*-



"""
Created on Sun Jan 17 15:34:13 2021

@author: akanksh.belchada
"""

"""PEP 498 introduced a new string formatting mechanism known 
as Literal String Interpolation or more commonly as F-strings 
(because of the leading f character preceding the string literal). 
The idea behind f-strings is to make string interpolation simpler.

print(f"{val}")
"""



"""Stack CHEAT SHEAT!!!!!!!!

Stack in Python can be implemented using following ways: 

list
collections.deque
queue.LifoQueue

"""

#Stack implementation using lists!
# A shortcoming of using List for implementing Stack is that it has
# speed issues as it grows
"""Reason being>>>>>>>The items in list are stored next to each other in memory, 
if the stack grows bigger than the block of memory that currently hold it, 
then Python needs to do some memory allocations.
 This can lead to some append() calls taking much longer than other ones."""
 
stack=[]
stack.append("a")
stack.append("b")
stack.append("c")

print(stack.pop())
print(stack)

#Implementation using collections.deque:
from collections import deque
myStack=deque()
myStack.append('a')
myStack.append('b')
myStack.append('c')
print('Initial Stack')
print(myStack)
myStack.popleft()       
myStack.pop()
print(myStack)
print(myStack[0])


#Implementation using queue module (LifoQueue)
from queue import LifoQueue
my_stack=LifoQueue(maxsize=3)


print("Here")
print(my_stack.qsize())                 #Print Size of the queue implemented using Queue module
my_stack.put(1)
my_stack.put(2)
my_stack.put(3)
my_stack.get()
print(my_stack.qsize())   
print("Full: ",my_stack.full())


#STACK IMPLEMENTATION USING SINGLY LINKED LIST
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
class Stack:
    def __init__(self):
        self.head=Node("head")
        self.size=0

    def __str__(self):
        out=""
        curr=self.head.next
        while curr:
            out+=str(curr.value)+ " ->"
            curr=curr.next
        return out[:-3]
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Peeking in an empty stack!")
        return self.head.next
    
    def push(self, value):
        node=Node(value)
        node.next=self.head.next
        self.head.next=node
        self.size+=1
        
    def pop(self):
        if self.isEmpty():
            raise Exception("Poping from an empty stack!")
        remove=self.head.next
        self.head.next=self.head.next.next
        return remove.value
    
    
if __name__=="__main__":
    print("LinkedList implementation of Stack")
    stack=Stack()
    stack.push(20)
    print(stack)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    print(stack)
    
    y=stack.pop()
    print(f"Current stack is {stack} and popped element is {y}")
    print(stack)   
        
    for i in range (1,11):
        stack.push(i)
    print(stack)
    print(stack.size)
            
        
        































