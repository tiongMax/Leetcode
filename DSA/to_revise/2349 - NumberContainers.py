from sortedcontainers import SortedSet
from collections import defaultdict
import heapq

# Using sortedSet
class NumberContainers:
    def __init__(self):
        self.index_to_num = {}
        self.num_to_index = defaultdict(SortedSet)

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_num:
            prev_num = self.index_to_num[index]
            self.num_to_index[prev_num].remove(index)
            if not self.num_to_index[prev_num]:
                del self.num_to_index[prev_num]

        self.index_to_num[index] = number
        self.num_to_index[number].add(index)

    def find(self, number: int) -> int:
        if number in self.num_to_index:
            return self.num_to_index[number][0]
        return -1

# Lazy pop for minHeap
class NumberContainers:
    def __init__(self):
        self.number_to_indices = defaultdict(list)
        self.index_to_numbers = {}

    def change(self, index: int, number: int) -> None:
        self.index_to_numbers[index] = number
        heapq.heappush(self.number_to_indices[number], index)

    def find(self, number: int) -> int:
        if not self.number_to_indices[number]:
            return -1

        while self.number_to_indices[number]:
            index = self.number_to_indices[number][0]
            if self.index_to_numbers.get(index) == number:
                return index

            heapq.heappop(self.number_to_indices[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)