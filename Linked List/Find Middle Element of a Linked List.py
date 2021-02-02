"""
Question Link: https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
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


def Middle_Element(head):
  if head is None:
    return

  fast = slow = head

  while fast is not None and fast.next is not None:
    fast = fast.next.next
    slow = slow.next
  
  return slow.data


head = Takeinput()
printLL(head)
print()
print(Middle_Element(head))