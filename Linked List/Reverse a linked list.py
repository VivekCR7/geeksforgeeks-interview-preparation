"""
Question Link: https://practice.geeksforgeeks.org/problems/reverse-a-linked-list/1
"""
class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

def Takeinput():
  curr_list = [int(ele) for ele in input().split()]
  head = tail = None

  for curr_data in curr_list:
    if curr_data == -1:
      break
    
    newnode = Node(curr_data)

    if head is None:
      head = tail = newnode
    else:
      tail.next = newnode
      tail = newnode
  
  return head

def printLL(head):
  while head is not None:
    if head.next:
      print(str(head.data)+"->",end="")
    else:
      print(str(head.data)+".",end="")
    head = head.next
  
  return 


#reverse a linked list iteratively
def reverseLL(head):
  prev = None
  curr = head

  while curr is not None:
    tail = curr.next
    curr.next = prev
    prev = curr
    curr = tail
  
  head = prev
  return head

#reverse linked list recursively 
def reverseLL_recursively(head):
  if head is None or head.next is None:
    return head

  smallhead = reverseLL_recursively(head.next)

  head.next.next = head
  head.next = None

  return smallhead

head = Takeinput()

head = reverseLL_recursively(head)
printLL(head)

