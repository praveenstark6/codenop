# Queue: class
class Queue:
  def __init__(self):
    self.queue = []
    self.size = 0
  
# enqueue
  def enqueue(self, data):
    self.queue.append(data)
    self.size += 1
  
# dequeue
  def dequeue(self):
    self.queue.pop(0)
    self.size -= 1

# front
  def front(self):
    return self.queue[0]

# rear
  def rear(self):
    return self.queue[-1]

# len
  def __len__(self):
    return self.size

# __str__
  def __str__(self):
    if self.size == 0:
      return "Queue is empty."
    result = ""
    for i in range(self.size):
      result += str(self.queue[i]) + "<-"
    return result


line = Queue()
line.enqueue(30)
line.enqueue(69)
line.enqueue(33)
print(line)
print(len(line))
line.dequeue()
print(line)
line.dequeue()
print(line)
