class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount
        self.d = {}
        for i in range(len(products)):
            self.d[products[i]] = prices[i]
        self.id = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.id += 1
        sum = 0
        for i in range(len(product)):
            sum += self.d[product[i]]*amount[i]
        if self.id % self.n == 0:
            sum = sum - (self.discount*sum)/100
        return sum


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)