# https://leetcode.com/explore/learn/card/heap/643/heap/4018/
import sys

# Min Heap: all nodes have smaller values than their child nodes
class MinHeap:
    def __init__(self, heapSize):
        self.heapSize = heapSize
        self.minheap = [0] * (heapSize + 1)
        self.realSize = 0

    def add(self, element):
        self.realSize += 1
        if self.realSize > self.heapSize:
            print("Add too many elements!")
            self.realSize -= 1
            return
        self.minheap[self.realSize] = element
        index = self.realSize
        parent = index // 2
        while (self.minheap[index] < self.minheap[parent] and index > 1):
            self.minheap[parent], self.minheap[index] = self.minheap[index], self.minheap[parent]
            index = parent
            parent = index // 2
    
    def peek(self):
        return self.minheap[1]
    
    def pop(self):
        if self.realSize < 1:
            print("Don't have any element!")
            return sys.maxsize
        else:
            removeElement = self.minheap[1]
            self.minheap[1] = self.minheap[self.realSize]
            self.realSize -= 1
            index = 1
            while (index < self.realSize and index <= self.realSize // 2):
                left = index * 2
                right = (index * 2) + 1
                if (self.minheap[index] > self.minheap[left] or self.minheap[index] > self.minheap[right]):
                    if self.minheap[left] < self.minheap[right]:
                        self.minheap[left], self.minheap[index] = self.minheap[index], self.minheap[left]
                        index = left
                    else:
                        self.minheap[right], self.minheap[index] = self.minheap[index], self.minheap[right]
                        index = right
                else:
                    break
            return removeElement
    
    def size(self):
        return self.realSize
    
    def __str__(self):
        return str(self.minheap[1 : self.realSize + 1])
        
# Max Heap: all nodes have bigger values than their child nodes
class MaxHeap:
    def __init__(self, heapSize):
        self.heapSize = heapSize
        self.maxheap = [0] * (heapSize + 1)
        self.realSize = 0

    def add(self, element):
        self.realSize += 1
        if self.realSize > self.heapSize:
            print("Add too many elements!")
            self.realSize -= 1
            return
        self.maxheap[self.realSize] = element
        index = self.realSize
        parent = index // 2
        
        while (self.maxheap[index] > self.maxheap[parent] and index > 1):
            self.maxheap[parent], self.maxheap[index] = self.maxheap[index], self.maxheap[parent]
            index = parent
            parent = index // 2
            
    def peek(self):
        return self.maxheap[1]
    
    def pop(self):
        if self.realSize < 1:
            print("Don't have any element!")
            return -sys.maxsize
        else:
            removeElement = self.maxheap[1]
            self.maxheap[1] = self.maxheap[self.realSize]
            self.realSize -= 1
            index = 1
            while (index < self.realSize and index <= self.realSize // 2):
                left = index * 2
                right = (index * 2) + 1
                if (self.maxheap[index] < self.maxheap[left] or self.maxheap[index] < self.maxheap[right]):
                    if self.maxheap[left] > self.maxheap[right]:
                        self.maxheap[left], self.maxheap[index] = self.maxheap[index], self.maxheap[left]
                        index = left
                    else:
                        self.maxheap[right], self.maxheap[index] = self.maxheap[index], self.maxheap[right]
                        index = right
                else:
                    break
            return removeElement
    
    def size(self):
        return self.realSize
    
    def __str__(self):
        return str(self.maxheap[1 : self.realSize + 1])



if __name__ == "__main__":
    print("Creating a new Min Heap")
    minHeap = MinHeap(5)
    minHeap.add(3)
    minHeap.add(1)
    minHeap.add(2)
    print(minHeap) # [1, 3, 2]
    print(minHeap.peek()) # 1
    print(minHeap.pop()) # 1
    print(minHeap.pop()) # 2
    print(minHeap.pop()) # 3
    minHeap.add(4)
    minHeap.add(5) 
    print(minHeap)

    print("\nCreating a new Max Heap")
    maxHeap = MaxHeap(5)    
    maxHeap.add(1)
    maxHeap.add(2)
    maxHeap.add(3)
    print(maxHeap) # [3, 1, 2]
    print(maxHeap.peek()) # 3
    print(maxHeap.pop()) # 3
    print(maxHeap.pop()) # 2
    print(maxHeap.pop()) # 1
    maxHeap.add(4)
    maxHeap.add(5)
    print(maxHeap) # [5,4]