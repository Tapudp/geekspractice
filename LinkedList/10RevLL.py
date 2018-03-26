class Node:
    #constructor to initalize the node object
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None

class LinkedList:
    #function to initialize the head
    def __init__(self):
        self.head = None
        
    #function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
    #function to insert new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #Utility function to print the LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

#Driver program to run the 
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print ("Given Linked List")
llist.printList()
llist.reverse()
print ("\nNow the reversed Linked List is ")
llist.printList()