# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.prefix_prod = [1]

    def add(self, num: int):
        if num == 0:
            self.prefix_prod = [1]
        else:
            self.prefix_prod.append(self.prefix_prod[len(self.prefix_prod) - 1] * num)

    def getProduct(self, k: int) -> int:
        if k > len(self.prefix_prod) - 1:
            return 0
        return (
            self.prefix_prod[len(self.prefix_prod) - 1] // 
            self.prefix_prod[len(self.prefix_prod) - 1 - k]
        )
    
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)