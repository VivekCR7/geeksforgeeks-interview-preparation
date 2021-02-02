"""

Question Link: https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1
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

#reverse k groups
def reverse(head,k):
  curr = head
  next = prev =None
  count = 0

  while curr is not None and count <k:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    count += 1

  if next is not None:
    head.next = reverse(next,k)

  return prev

head = Takeinput()
head = reverse(head,3)
printLL(head)