# Stack
class Stack:
  def __init__(self):
    self.stack = []
    self.size = 0
  
# push
  def push(self, data):
    self.stack.append(data)
    self.size += 1
  
# pop
  def pop(self):
    self.stack.pop()
    self.size -= 1

# peek
  def peek(self):
    return self.stack[-1]

# len
  def __len__(self):
    return self.size

# __str__
  def __str__(self):
    result = ""
    for i in range(self.size):
      result += str(self.stack[i]) + "->"
    return result


num = Stack()
num.push(70)
num.push(58)
print(num)
num.pop()
num.push(30)
num.push(2)
print(len(num))
print(num)

