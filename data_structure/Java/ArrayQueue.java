package Java;

import java.util.*;

@SuppressWarnings("unchecked")
public class ArrayQueue<T> implements QueueInterface<T>, Iterable<T> {
	private static final int DEFAULT_CAPACITY = 10;
	private int cap,	// total number of elements in the queue
                cur,		// current number of elements
                front,  	// front index
                back;		// back index
	private T[] arr;

	/**
	*  Creates a new empty queue.
	*/
	public ArrayQueue () {
		cap = DEFAULT_CAPACITY;
		arr = (T[]) new Object[DEFAULT_CAPACITY];
		back = -1; 
        front = 0;
	}

	/**
	*  Tests if the queue is logically empty.
	*
	*  @return true if the queue is empty and false otherwise
	*/
	public boolean isEmpty() {
		return cur == 0;
	}

	/**
	*  Puts a value into the back of the queue. It works with wraparound.
	*  If the queue is full, it doubles its size.
	*
	*  @param value the item to insert.
	*/
	public void enqueue (T value) {
		if (isFull()) doubleSize();

		back++;
		arr[back%cap] = value;
		cur++;
	}

	/**
	*  Returns the first element in the queue.
	*
	*  @return element at front of the queue
	*  @throws NoSuchElementException if the queue is empty.
	*/
	public T getFront()
	{
		if (isEmpty())
			throw new QueueException();
		else
			return arr[front%cap];
	}

	/**
	*  Returns and removes the front element of the queuee. It works with wraparound.
	*
	*  @return element at front of the queue
	*  @throws NoSuchElementException if the queue is empty.
	*/
	public T dequeue() {
		T t = getFront();
		arr[front%cap] = null; // for garbage collection
		front++;
		cur--;
		return t;
	}

	/**
	*  Makes the queue physically empty.
	*
	*/
	public void clear() {
		for(int i = 0; i < cap; i++) {
            arr[i] = null;
        }

		cur = 0; back = -1; front = 0;
	}

	/**
	*  Tests if the queue is logically full
	*/
	public boolean isFull()
	{
		return cur == cap;
	}

	/**
	*  Increase the queue capacity by doubling the size.
	*/
	private void doubleSize()
	{
		T[] newArray = (T[]) new Object[2*cap];

		//copy items
		for(int i = front; i <= back; i ++)
			newArray[i-front] = arr[i%cap];

		arr = newArray;
		front = 0;
		back = cur-1;
		cap *= 2;
	}

 /***************    Iterator      *************** */

	/**
	* Obtains an Iterator object used to traverse the Queue from its front to back.
	*
	* @return an iterator.
	*
	* @throws UnsupportedOperationException if you remove using the iterator
	*/
	public Iterator<T> iterator() {
		return new QueueIterator();
	}

	private class QueueIterator implements Iterator<T> {
		private int index;      //traversal index


		/**
		*  Create a new empty iterator.
		*/
		public QueueIterator() {
			index = front;
		}

		/**
		*  Tests if there are more items in the Queue
		*
		*/
		public boolean hasNext() {
			return index <= back;
		}

		/**
		*  Returns the next item in the Queue.
		*
		*/
		public T next() {
			return arr[(index++)%cap];
		}

		/**
		*  Remove is not implemented
		*
		*/
		public void remove() {
			throw new java.lang.UnsupportedOperationException();
		}
	}

	public static void main(String[] args) {
		ArrayQueue<String> queue = new ArrayQueue<String>();

		String[] people = {"Tom", "Jay", "Pat", "Meghan", "Tom", "Mark", "Kasey", "John", "Helen"};

		for (int i = 0; i < people.length; i++)
			queue.enqueue(people[i]);

		for (int i = 0; i < 2; i++) {
            queue.dequeue();
        }

		Iterator itr = queue.iterator();
		while(itr.hasNext())
			System.out.println(itr.next());

		System.out.println("=================");
		queue.enqueue("Mike");
		queue.enqueue("Bev");

		itr = queue.iterator();
		while(itr.hasNext())
			System.out.print(itr.next() + " ");

		System.out.println();
   }
}

	/**              QueueInterface           **/

interface QueueInterface<T> {
	/**
	* Tests if the Queue is empty.
	*/
	public boolean isEmpty();

	/**
	*  Removes and returns the front item
	*/
	public T dequeue() throws QueueException;

	/**
	*  Returns the front item without its removal
	*/
	public T getFront() throws QueueException;

	/**
	* Inserts an item to teh back
	*/
	public void enqueue(T t);

	/**
	* Removes all items from the Queue.
	*/
	public void clear();
}


	/**              QueueException           **/

class QueueException extends RuntimeException {
	public QueueException(String name) {
		super(name);
	}

	public QueueException() {
		super();
	}
}
