import heapq

class MedianFinder:

    def __init__(self):
        self.leftHalf = []
        self.rightHalf = []

    def addNum(self, num: int) -> None:
        if self.rightHalf and num > self.rightHalf[0]:
            heapq.heappush(self.rightHalf, num)
        else:  
            heapq.heappush(self.leftHalf, -num)
        
        if len(self.leftHalf) > len(self.rightHalf) + 1:
            heapq.heappush(self.rightHalf, -heapq.heappop(self.leftHalf))
        if len(self.rightHalf) > len(self.leftHalf) + 1:
            heapq.heappush(self.leftHalf, -heapq.heappop(self.rightHalf))

    def findMedian(self) -> float:
        if len(self.leftHalf) > len(self.rightHalf):
            return -self.leftHalf[0]
        elif len(self.rightHalf) > len(self.leftHalf):
            return self.rightHalf[0]
        return (-self.leftHalf[0] + self.rightHalf[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()