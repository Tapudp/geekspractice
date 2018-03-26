class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        return self.items.append()

    def addRear(self, item):
        return self.items.insert(0, item)

    def removeFront(self, item):
        return self.items.pop()

    def removeRear(self, item):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

        