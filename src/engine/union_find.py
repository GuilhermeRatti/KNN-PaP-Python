class UnionFind():
    def __init__(self, length:int, **kwargs):
        self.length = length
        self.list = [i for i in range(self.length)]
        self.weights = [1]*self.length
        self.path_compression = kwargs.get("path_compression", True)
    
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
            if self.path_compression:
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
            # print(f"tried to connect {idx1} and {idx2} but they're already in the same group!")
            return ValueError
        
        if self.weights[grp1] < self.weights[grp2]:
            self.list[grp1] = grp2
            self.weights[grp2] += self.weights[grp1]
        else:
            self.list[grp2] = grp1
            self.weights[grp1] += self.weights[grp2]

    # def remove(self,idx1:int,idx2:int):
    #     assert self.path_compression is not True, "Can't perform remove action with path compression active."

    #     if self.list[idx1] == idx2:
    #         self.list[idx1] = idx1
    #     elif self.list[idx2] == idx1:
    #         self.list[idx2] == idx2
    #     else:
    #         msg = f"indexes are not connected directly! {idx1} - {idx2}."
    #         raise IndexError(msg)

        
    def standardize_groups(self):
        """
        Standardize the values of every group into one single value for each group, which is not always granted before performing this operation (a single group may be indexes by multiple values).
        """
        for idx in range(self.length):
            self.list[idx] = self.find(idx)

    def get_uniques(self):
        return set(self.list)

    def __repr__(self):
        """
        Return a string representation of the heap.
        """
        return f"UnionFind: {[(a,b) for a, b in zip(self.list,self.weights)]}"
    
    
        
