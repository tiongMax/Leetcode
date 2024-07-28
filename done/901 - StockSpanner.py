# https://leetcode.com/problems/online-stock-span/

class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cons_day = 1
        while self.stack and self.stack[-1][0] <= price:
            p, d = self.stack.pop()
            cons_day += d
            
        self.stack.append((price, cons_day))
        return cons_day

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)