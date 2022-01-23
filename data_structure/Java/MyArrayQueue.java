package Java;

public class MyArrayQueue<T> implements QueueInterface<T> {
    private T[] contents;
    private int front;
    private int rear;
    private int cur;
    private int cap;
    private static final int DEFAULT_CAPACITY = 50;

    public MyArrayQueue() {
        this(DEFAULT_CAPACITY);
    }

    @SuppressWarnings("unchecked")
    public MyArrayQueue(int initialCapacity) {
        contents = (T[])new Object[initialCapacity + 1];
        front = 0;
        rear = contents.length - 1;
    }


    @Override
    public void enqueue(T newEntry) {
        if (isFull()) doubleSize();
        rear++;
        contents[rear%cap] = newEntry;
        cur++;
    }


    @Override
    public T dequeue() {
        T e = getFront();
        contents[front%cap] = null;
        front++;
        cur--;
        return e;
    }


    @Override
    public T getFront() {
        if (isEmpty()) {
            throw new IllegalStateException();
        }
        return contents[front];
    }


    @Override
    public boolean isEmpty() {
        return (((rear + 1) % contents.length) == front);
    }


    public boolean isFull() {
        return cur == cap;
    }


    @Override
    public void clear() {
        while (!isEmpty()) {
            dequeue();
        }
    }

    @SuppressWarnings("unchecked")
    private void doubleSize() {
        T[] newArray = (T[]) new Object[2*cap];

        //copy items
        for(int i = front; i <= rear; i ++)
            newArray[i-front] = contents[i%cap];
        contents = newArray;
        front = 0;
        rear = cur-1;
        cap *= 2;
    }
}