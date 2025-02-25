class ProdSum:
    def __init__(self):
        self.prod_sum = [1]
        self.last_zero_index = 0
        self.count = 0

    def add(self, num):
        if num == 0:
            self.prod_sum.append(1)
            self.count += 1
            self.last_zero_index = self.count
        else:
            latest_prod = self.prod_sum[-1]
            self.prod_sum.append(latest_prod * num)
            self.count += 1

    def get_prod(self, k):
        eff_idx = self.count - k
        if eff_idx < self.last_zero_index:
            print(0)
        else:
            print(self.prod_sum[-1] // self.prod_sum[-(k + 1)])


p = ProdSum()
p.add(3)
p.add(0)
p.add(2)
p.add(5)
p.add(4)
p.get_prod(2)
p.get_prod(3)
p.get_prod(4)
p.add(8)
p.get_prod(2)
