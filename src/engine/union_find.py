class UnionFind():
    def __init__(self, length:int):
        self.length = length
        self.list = [i for i in range(self.length)]
        self.weights = [1]*self.length
    
    def find(self, idx:int) -> int:
        """
        Finds the group value of the provided index
        
        Args:
            idx (int): The index to find the group of.
            
        Returns:
            int: The value of the group head.
        """
        # while the root doesnt point to itself (not the root of the group)
        while idx != self.list[idx]:
            # performing halving (path compression) to increase efficiency
            self.list[idx] = self.list[self.list[idx]]
            idx = self.list[idx]

        return idx
    
    def union(self, idx1:int, idx2:int):
        """
        Performs union between two groups by index.
        
        Args:
            idx1 (int): The idx of element 1 to perform union

            idx2 (int): The idx of element 2 to perform union
            
        Returns:
            ValueError: Returns ValueError in case of circular connection attempt, otherwise returns nothing
        """
        grp1, grp2 = self.find(idx1), self.find(idx2)
        
        # we must avoid circular connections
        if grp1 == grp2:
            return ValueError

        if self.weights[grp1] < self.weights[grp2]:
            self.list[grp1] = grp2
            self.weights[grp2] += self.weights[grp1]
        else:
            self.list[grp2] = grp1
            self.weights[grp1] += self.weights[grp2]

        
    def __repr__(self):
        """
        Return a string representation of the heap.
        """
        return f"UnionFind: {[(a,b) for a, b in zip(self.list,self.weights)]}"
