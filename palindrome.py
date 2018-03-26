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

def palChecker(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

        return stillEqual

print(palChecker("madam"))
print(palChecker("tata"))
print(palChecker('radar'))