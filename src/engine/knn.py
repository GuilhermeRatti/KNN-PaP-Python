from .union_find import UnionFind
from ..edge import Edge
from .heap import Heap
from ..utils import get_masked_indices

class KNN():
    def __init__(self, intput_list:list, k:int=2):
        self.k = k
        self.intput_list = intput_list
        self.groups_control = UnionFind(len(self.intput_list))
        self._groups_defined = 0
    
    def define_groups(self):

        priority_queue_list = []
        for i in range(len(self.intput_list)):
            weights = [Edge(self.intput_list[i], self.intput_list[j]) for j in range(len(self.intput_list)) if j!=i]
            priority_queue_list.append(Heap(weights))
            
        connected_edges = Heap(heapify=False,heap_type='max')
        curr_vertex = 0
        counter = len(self.intput_list) - 1
        
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
        
        for i in range(self.k - 1):
            connected_edges.extract()

        
        del self.groups_control

        self.groups_control = UnionFind(len(self.intput_list))

        for _edge in connected_edges:
            self.groups_control.union(_edge.id1,_edge.id2)

        self._groups_defined = 1
        
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