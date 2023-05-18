
class Cart:
    def __init__(self, product_name, quantity, price, action):
        self.product_name = product_name
        self.quantity = quantity
        self.price=price
        self.action=action
#updating stock
    def new_stock_levels(self,new_product):
        self.product_name=new_product
# updating stock quantity
    def Quantity_products(self,new_quantity):
        self.quantity=new_quantity
# updating prices for goods
    def pricing(self, new_price):
        self.price=new_price
    def update_action(self,needed_action):
       self.action=needed_action
    def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price},{self.action}"