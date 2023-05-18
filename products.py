
class Cart:
    def __init__(self, product_name, quantity, price, action):
        self.product_name = product_name
        self.quantity = quantity
        self.price=price
        self.action=action

    def update_new_stock(self,new_product):
        self.product_name=new_product

    def update_quantity(self,new_quantity):
        self.quantity=new_quantity

    def update_pricing(self, new_price):
        self.price=new_price
    def update_action(self,new_action):
       self.action=new_action
    def __str__(self):
        return f"{self.product_name},{self.quantity},{self.price},{self.action}"
    
    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += quantity
                return
        item = Cart_Item(product, quantity)
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def update_quantity(self, item, quantity):
        item.quantity = quantity

    def get_total_items(self):
        total_items = sum(item.quantity for item in self.items)
        return total_items
    
    def calculate_total_price(self):
        total_price = sum(item.product.price * item.quantity for item in self.items)
        return total_price    