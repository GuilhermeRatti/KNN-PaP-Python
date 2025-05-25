from .vertex import Vertex

class Edge():
    def __init__(self, *args):
        """
        Initialize an edge between two vertices.
        The edge is represented by the two vertices it connects and the weight
        which is the distance between them.
        Args:
            args (tuple): A tuple containing two Vertex instances.
        """
        if len(args) != 2:
            raise ValueError("Edge must be initialized with exactly two Vertex instances.")
        if not all(isinstance(arg, Vertex) for arg in args):
            raise TypeError("Both arguments must be instances of Vertex.")
        
        vertex1 = args[0]
        vertex2 = args[1]
        
        # Assigning the id and weight of the edge
        # the distance between the two vertexes
        self.id1 = vertex1.id
        self.id2 = vertex2.id
        self.weight = vertex1.distance(vertex2)
    
    # Overload subtraction operator
    def __sub__(self, other):
        if isinstance(other, Edge):
            return self.weight - other.weight
        
        return NotImplementedError("Subtraction can only be performed between two Edge instances.")

    # Overload less than (<) operator
    def __lt__(self, other):
        if isinstance(other, Edge):
            if self.weight != other.weight:
                return self.weight < other.weight
            elif self.id1 != other.id1:
                return self.id1 < other.id1
            elif self.id2 != other.id2:
                return self.id2 < other.id2
            else:
                raise ValueError(f"Edges are equal in every way, cannot compare. f{self} and {other}")
        return NotImplementedError("Less than comparison can only be performed between two Edge instances.")
    
    # Overload greater than (>) operator
    def __gt__(self, other):
        if isinstance(other, Edge):
            if self.weight != other.weight:
                return self.weight > other.weight
            elif self.id1 != other.id1:
                return self.id1 > other.id1
            elif self.id2 != other.id2:
                return self.id2 > other.id2
            else:
                raise ValueError(f"Edges are equal in every way, cannot compare. f{self} and {other}")
        return NotImplementedError("Greater than comparison can only be performed between two Edge instances.")

    def __repr__(self):
        """
        Return a string representation of the edge.

        """
        return f"{self.id1+1} {self.id2+1} {self.weight}"