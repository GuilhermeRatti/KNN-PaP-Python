import math

class Vertex():
    def __init__(self, **kwargs):
        self.id = int(kwargs.get('id')) - 1
        self.coordinates = kwargs.get('coordinates')

    def distance(self, other) -> float:
        """
        Calculate the Euclidean distance between two vertices.
        
        Args:
            other (Vertex): The other vertex to calculate the distance to.
            
        Returns:
            float: The Euclidean distance between the two vertices.
        """
        if isinstance(other, Vertex):
            return math.sqrt(sum((a - b) ** 2 for a, b in zip(self.coordinates, other.coordinates)))
        
        return NotImplementedError("Distance can only be calculated between two Vertex instances.")

    # Overload less than (<) operator
    def __lt__(self, other):
        if isinstance(other, Vertex):
            return self.id < other.id
        return NotImplementedError("Less than comparison can only be performed between two Vertex instances.")
    
    # Overload greater than (>) operator
    def __gt__(self, other):
        if isinstance(other, Vertex):
            return self.id > other.id
        return NotImplementedError("Greater than comparison can only be performed between two Vertex instances.")
    
    def __repr__(self):
        """
        Return a string representation of the edge.

        """
        return f"{self.id + 1}"
