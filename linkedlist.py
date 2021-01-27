# Node
class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

# linked list
class LinkedList:
  def __init__(self):
    self.head = Node()
    self.size = 0

  
# addlast
  def addLast(self, data):
    self.size += 1
    if self.head.data is None:
      self.head = Node(data, None)
      return 
    this = self.head
    while this and this.next:
      this = this.next
    this.next = Node(data, None) 
  
# addfront
  def addFront(self, data): # 8->5->4->6  8
    self.size += 1
    if self.head.data is None:
      self.head = Node(data, None)
      return 
    self.head = Node(data, self.head)

# removelast
  def removeLast(self):
    if self.head.data is None:
      return 
    self.size -= 1
    this = self.head 
    while this and this.next:
      if this.next.next == None:
        break
      this = this.next
    this.next = None
# removefront
  def removeFront(self):
    if self.head.data is None:
      return 
    self.size -= 1
    self.head = self.head.next
# __str__
  def __str__(self):
    if self.head.data is None:
      return "LinkedList is empty."
    result = ""
    this = self.head
    while this and this.next:
      result += str(this.data) + "->"
      this = this.next
    return result + str(this.data)

# size
  def __len__(self):
    return self.size


l = LinkedList()
l.addFront(45)
l.addLast(90)
print(l)
l.addLast(67)
l.addFront(78)
print(l)
l.removeFront()
print(l)
print(len(l))
l.removeLast()
print(l)

