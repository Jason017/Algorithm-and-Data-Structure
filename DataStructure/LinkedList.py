class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)

print('Given LinkedList: ')
llist.printList()

print('\nReversed LinkedList: ')
llist.reverse()
llist.printList()

