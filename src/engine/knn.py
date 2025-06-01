from .union_find import UnionFind
from ..edge import Edge
from .heap import Heap
from ..utils import get_masked_indices

class KNN():
    def __init__(self, intput_list:list, k:int=2):
        """
        Initialize the KNN algorithm with a list of vertices and the number of clusters (k).
        Args:
            intput_list (list): A list of Vertex objects.
            k (int): The number of clusters to form. Default is 2.
        """

        self.k = k
        self.intput_list = intput_list
        self.groups_control = UnionFind(len(self.intput_list))
        self._groups_defined = 0
    
    def define_groups(self):
        """
        Define the groups based on the KNN algorithm.
        This method constructs clusters using a priority queue and the Union-Find data structure.
        It connects every vertex to it's nearest, non-connected vertex until all vertices are connected. Then it extracts the k-1 largest edges to form the final clusters.
        """
        
        
        priority_queue_list = []
        
        # Create a priority queue for each vertex, containing edges to all other vertices
        for i in range(len(self.intput_list)):
            weights = [Edge(self.intput_list[i], self.intput_list[j]) for j in range(len(self.intput_list)) if j!=i]
            priority_queue_list.append(Heap(weights))
            
        # Create a max-heap to store the connected edges
        # This will store the edges that connect the vertices in the final clusters
        # The max-heap will be used to extract the k-1 largest edges
        connected_edges = Heap(heapify=False,heap_type='max')
        curr_vertex = 0
        counter = len(self.intput_list) - 1
        
        # While there are still edges to connect, extract the minimum edge from the respective index in the list of priority queue
        while counter > 0:
            curr_edge = priority_queue_list[curr_vertex].extract()
            if self.groups_control.union(curr_edge.id1, curr_edge.id2) != ValueError:
                counter -= 1
                if curr_edge.id1 != curr_vertex:
                    curr_vertex = curr_edge.id1
                elif curr_edge.id2 != curr_vertex:
                    curr_vertex = curr_edge.id2
                else:
                    raise f"Current edge does not have the current vertex, something is wrong. {curr_edge} - {curr_vertex}"
                connected_edges.insert(curr_edge)
        
        # After all vertices are connected, we need to extract the k-1 largest edges from the connected edges
        for i in range(self.k - 1):
            connected_edges.extract()

        # After extracting the k-1 largest edges, we can define the groups based on the remaining edges
        # Deleting the old groups_control union find instance. We will create a new one with the connected edges
        del self.groups_control
        self.groups_control = UnionFind(len(self.intput_list))

        # Now we can union the remaining edges to form the final clusters
        # We will iterate through the connected edges and union the vertices in each edge
        for _edge in connected_edges:
            self.groups_control.union(_edge.id1,_edge.id2)

        # After all edges are processed, we can mark the groups as defined
        self._groups_defined = 1
        
        # Clean up the memory by deleting the priority queue list and connected edges
        del priority_queue_list
        del connected_edges
        

    def get_groups(self):
        assert self._groups_defined == 1, "You must define the groups beforehand!"

        self.groups_control.standardize_groups()

        # get unique values from groups
        groups_set = self.groups_control.get_uniques()
        
        output_list = []
        for group in groups_set:
            curr_group = get_masked_indices(self.intput_list, [i == group for i in self.groups_control.list])
            list(curr_group).sort()
            output_list.append(curr_group)
        
        output_list.sort()
        return output_list