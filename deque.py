# deque: class
class Deque:
  def __init__(self):
    self.deque = []
    self.size = 0
  # addfront
  def addfront(self, data):
    self.deque.insert(0, data)
    self.size += 1

  # addlast
  def addlast(self, data):
    self.deque.append(data)
    self.size += 1

  # removefront
  def removefront(self):
    self.deque.pop(0)
    self.size -= 1

  # removelast
  def removelast(self):
    self.deque.pop()
    self.size -= 1

  # front
  def front(self):
    return self.deque[0]

  # rear
  def rear(self):
    return self.deque[-1]

  # __len__
  def __len__(self):
    return self.size

  # __str__
  def __str__(self):
    if self.size == 0:
      return "deque is empty"
    result = ""
    for i in range(self.size):
      result += str(self.deque[i]) + "<-"
    return result


line = Deque()
line.addfront(45)
line.addlast(56)
print(line)
line.addlast(98)
line.addfront(9)
print(line)
line.removelast()
line.removefront()
print(line)
print(len(line))
line.removefront()
print(line)
