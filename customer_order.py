class Customer_order:
    def __init__(self,name,price,items_ordered):
        self.name = name
        self.price = price
        self.items_ordered = items_ordered
    def total_order(self):
        sum = 0
        for p in self.price:
            sum += p
            return sum
        print(f"Get your total {self.total_order}")
    def list_proucts(self):
        add = []
        for item in self.items_ordered:
            if item == items_ordered:
                add.append(item)
        return add