
class Cart:
    def __init__(self, product_name, quantity, price, action):
        self.product_name = product_name
        self.quantity = quantity
        self.price=price
        self.action=action
#updating stock
    def update_new_stock(self,new_product):
        self.product_name=new_product
# updating stock quantity
    def update_quantity(self,new_quantity):
        self.quantity=new_quantity
# updating prices for goods
    def update_pricing(self, new_price):
        self.price=new_price
    def update_action(self,new_action):
       self.action=new_action
    def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price},{self.action}"