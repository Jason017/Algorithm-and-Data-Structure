class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next
    
    def reverse_node(self):
        prev = None
        curr = self
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def print_llist(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def copy_llist(self):
        temp = self.head
        new_llist = LinkedList()
        while temp:
            new_node = Node(temp.data)
            new_node.next = new_llist.head
            new_llist.head = new_node
            temp = temp.next
        new_llist.reverse()
        return new_llist

    def to_list(self):
        ans = []
        head = self.head
        while head:
            ans.append(head.data)
            head = head.next
        return ans

def to_linkedList(aList):
    new_llist = LinkedList()
    for i in aList:
        new_llist.push(i)
    new_llist.reverse()
    return new_llist

llist = LinkedList()
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)

print('Given LinkedList: ')
llist.print_llist()

print('\nReversed LinkedList: ')
llist.reverse()
llist.print_llist()

# llist2 = to_linkedList([54,24,67,89])
# print('\nLinkedList to list')
# llist2.print_llist()
# print(llist2.to_list())

# print('\nCopied LinkedList: ')
# copy = llist.copy_llist()
# copy.print_llist()


def reverse(head):
    prev = None
    curr = head
    while curr:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev

def to_llist(aList):
    head = answer = Node(0)
    for i in aList:
        newnode = Node(i)
        head.next = newnode
        head = head.next
    return answer.next

