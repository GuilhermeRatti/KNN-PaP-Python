class Heap():
    def __init__(self, elements_list: list = [], **kwargs):
        """
        Initialize a heap data structure.

        Args:
            elements_list (list): A list of elements to initialize the heap with.
            **kwargs: Additional keyword arguments for heap initialization:
                - heapify - True (default)
                - heap_type - 'min' (default)
        """
        # Initialize the heap with the provided keyword arguments

        self.heap = elements_list
        self.size = len(self.heap)
        self.heap_type = kwargs.get('heap_type', 'min')
        self.heapify = kwargs.get('heapify', True)
        if self.heapify:
            self.build_heap()
        
    def build_heap(self):
        """
        Build the heap from the provided elements.
        """
        # Build the heap by calling _heapify_down on each non-leaf node
        for i in range(self.size // 2, -1, -1):
            self._heapify_down(i)

    def insert(self, element):
        """
        Insert a new element into the heap.

        Args:
            element: The element to be inserted into the heap.
        """
        # Insert a new element into the heap and maintain the heap property
        self.heap.append(element)
        self.size += 1
        self._heapify_up(self.size - 1)

    def extract(self) -> object:
        """
        Extract the root element from the heap.

        Returns:
            The root element of the heap.
        """
        # Extract the root element from the heap and maintain the heap property
        if self.size == 0:
            raise IndexError("Heap is empty")

        self.heap[0], self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        root = self.heap.pop()
        self.size -= 1
        self._heapify_down(0)

        return root

    def _heapify_up(self, index: int):
        """
        Shift up the element at the given index to maintain the heap property.

        Args:
            index (int): The index of the element to shift up.
        """
        # Shift up the element at the given index to maintain the heap property
        parent = (index - 1) // 2

        if self.heap_type == 'min':
            if index > 0 and self.heap[index] < self.heap[parent]:
                # Swap the elements and recursively heapify the parent
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self._heapify_up(parent)
        else:
            if index > 0 and self.heap[index] > self.heap[parent]:
                # Swap the elements and recursively heapify the parent
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self._heapify_up(parent)

    def _heapify_down(self, index: int):
        """
        Maintain the heap property by shifting down the element at the given index.

        Args:
            index (int): The index of the element to shift down.
        """
        # Shift down the element at the given index to maintain the heap property
        higher_priority = index
        left = 2 * index + 1
        right = 2 * index + 2

        if self.heap_type == 'min':
            if left < self.size and self.heap[left] < self.heap[higher_priority]:
                higher_priority = left
            if right < self.size and self.heap[right] < self.heap[higher_priority]:
                higher_priority = right
        else:
            if left < self.size and self.heap[left] > self.heap[higher_priority]:
                higher_priority = left
            if right < self.size and self.heap[right] > self.heap[higher_priority]:
                higher_priority = right

        if higher_priority != index:
            # Swap the elements and recursively heapify the affected subtree
            self.heap[index], self.heap[higher_priority] = self.heap[higher_priority], self.heap[index]
            self._heapify_down(higher_priority)

    def __repr__(self):
        """
        Return a string representation of the heap.
        """
        msg = f"Heap list ({self.heap_type}):\n"
        for i in range(self.size):
            msg += f"\t{i} - {self.heap[i]}\n"
        if self.size == 0:
            msg += "\t<empty heap>"

        return msg()