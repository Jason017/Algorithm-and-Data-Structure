package Java;

public class LinkedList {
    private Node head;

    private static class Node {
        private int val;
        private Node next;
        Node(int x) {
            this.val = x;
            this.next = null;
        }
    }

    public static LinkedList insert(LinkedList llist, int val) {
        Node newNode = new Node(val);
        newNode.next = null;

        if (llist.head == null) {
            llist.head = newNode;
        } else {
            Node curr = llist.head;
            while (curr.next != null) {
                curr = curr.next;
            }
            curr.next = newNode;
        }
        return llist;
    }

    public static void printList(LinkedList list) {
        Node currNode = list.head;
        System.out.print("LinkedList: ");
        while (currNode != null) {
            System.out.print(currNode.val + " ");
            currNode = currNode.next;
        }
    }

    public static void main(String[] args) {

        LinkedList llist = new LinkedList();
    
        llist = insert(llist, 1);
        llist = insert(llist, 2);
        llist = insert(llist, 3);
        llist = insert(llist, 4);
        llist = insert(llist, 5);
        llist = insert(llist, 6);
        llist = insert(llist, 7);
        llist = insert(llist, 8);

        printList(llist);
    }
}
