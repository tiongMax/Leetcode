# https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo:
    def __init__(self):
        self.overlap1 = []
        self.overlap2 = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap2:
            if end > s and e > start:
                return False

        for s, e in self.overlap1:
            if end > s and e > start:
                self.overlap2.append((max(start, s), min(end, e)))

        self.overlap1.append((start, end))
        return True 

        
# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)