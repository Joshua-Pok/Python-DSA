# A Heap has 2 types: MinHeap and MaxHeap
# Depending min/max, each child of the node has to be either larger(minheap) or smaller(maxheap) than the parent
# All subtrees of minheaps are also minheaps, likewise all subtrees of maxheaps are also maxheaps
# A priority queue is a abstract data structure that cna be implemented with a heap.
# We can remove the root node, take the last node, put it at the top. Then we sift down
# When adding a new element, we append it to the heap, we sift up

# btw heaps are just arrays lol.

class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)


    def __repr__(self):
        return str(self.heap)

    def insert(self, key, value):
        # add to the end
        self.heap.append((key, value))
        #sift up
        self.siftup(len(self.heap) - 1)

    def peek_min(self):
        if not self.heap:
            raise IndexError("Empty Heap")
        return self.heap[0] #min element is always the root

    def extract_min(self):
        if not self.heap:
            raise IndexError('Empty Heap')
        min_element = self.heap[0]
        last_element = self.heap.pop() # take last element 

        if self.heap
            self.heap[0] = last_element #put it at the top
            self.siftdown(0) #sift down
        return min_element

    def heapify(self, elements): # takes a list of values and order them as a heap
        self.heap = list(elements)


        for i in reversed(range(self._parent(len(self.heap) - 1) + 1)): # getting parent of last elemtn and go ( all leaf nodes are valid heaps and go from bottom up to siftdown, meaning push down if necessary to restrore min heap property.)
            self.siftdown(i)

    def meld(self, other_heap):
        pass

    def _parent(self, index): # (index - 1) // 2
        return (index + 1) // 2 if index != 0 else None

    def _left(self, index): # 2 * index + 1
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    def _right(self, index): # 2 * index + 2
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    def siftup(self, index):
        parent_index = self._parent(index)
        while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = self._parent(index)

    def siftdown(self, index): 
        while True: #keep looping until element is in the correct position 
            smallest = index #assume current node is the smallest among itself and children

            left = self._left(index) #get left child
            right = self._right(index) #get right child

            if left is not None and self.heap[left][0] < self.heap[smallest][0]: #if left child exists and is smaller than smallest, update smallest to left.

                smallest = left

            if right is not None and self.heap[right][0] < self.heap[smallest][0]: #if right child exists and is smaller than smallest, update smallest to right

                smallest = right

            if smallest == index: #we already satisfied condition, exit

                break

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index] #swap current index with smallest

            index = smallest #update index to smallest
