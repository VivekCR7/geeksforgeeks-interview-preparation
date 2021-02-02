"""
Question Link: https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1
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

# rotate a linked list
def length(head):
  if head is None:
    return 0
  return 1+length(head.next)

def rotate(head,k):
  if k == 0:
    return

  curr = head
  count = 1

  while count<k and curr is not None:
    curr = curr.next
    count += 1

  if curr is None:
    return

  kthnode= curr
  while curr.next is not None:
    curr = curr.next

  curr.next = head
  head = kthnode.next
  kthnode.next = None

  return head

head = Takeinput()
printLL(head)
print()

head = rotate(head,3)
printLL(head)

