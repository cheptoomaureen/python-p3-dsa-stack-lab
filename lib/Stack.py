class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        return len(self.items) == 0
        pass

    def push(self, item):
       if len(self.items) < self.limit:
           self.items.append(item)
       else:
           print("Stack Overflow")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None 
        pass

    def peek(self):
        if not self.isEmpty(self.items):
            return self.items[-1]
        pass
    
    def size(self):
        return len(self.items)

        pass

    def full(self):
        return len(self.items) == self.limit
        pass

    def search(self, target):
        try:
            return len(self.items) - self.items.index(target) - 1
        except ValueError:
            return -1
        pass
