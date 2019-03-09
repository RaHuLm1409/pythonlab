class Stack:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def size(self):
         return len(self.items)
o=Stack()
o.isEmpty()
o.push(25)
o.push(14)
o.push(23)
o.push(10)
o.push(22)
o.size()
o.pop()
o.pop()
print(o.items)
