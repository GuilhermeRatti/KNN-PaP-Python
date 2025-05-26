from .union_find import UnionFind
from ..edge import Edge
from .heap import Heap
from ..utils import get_masked_indices

class Kruskal():
    def __init__(self, intput_list:list, k:int=2):
        self.k = k
        self.intput_list = intput_list
        self.groups_control = UnionFind(len(self.intput_list))
        self._groups_defined = 0

    def define_groups(self):
        weights = [Edge(self.intput_list[i], self.intput_list[j]) for i in range(len(self.intput_list)) for j in range(i + 1, len(self.intput_list))]
        
        # print(len(self.intput_list))
        # print(len(weights))

        priority_queue = Heap(weights)
        count = len(self.intput_list) - self.k

        while count > 0:
            new_edge = priority_queue.extract()

            if self.groups_control.union(new_edge.id1, new_edge.id2) is not ValueError:
                count-=1

        self._groups_defined = 1
        # freeing space since these 2 data structures gobble up a lot of memory
        del weights
        del priority_queue

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