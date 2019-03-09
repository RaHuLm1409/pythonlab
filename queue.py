class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

o=Queue()
o.isEmpty()
o.enqueue(25)
o.enqueue(14)
o.enqueue(23)
o.enqueue(10)
o.enqueue(22)
o.size()
o.dequeue()
o.dequeue()
print(o.items)
