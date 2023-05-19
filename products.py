
class Cart:
    def __init__(self):
        self.inventory = {"fruits": {}, "vegitables": {}}
    def add_product(self, category, product_name, price, quantity):
        if category in self.inventory:
            if product_name in self.inventory[category]:
                self.inventory[category][product_name]["price"] = price
                self.inventory[category][product_name]["quantity"] += quantity
            else:
                self.inventory[category][product_name] = {"price": price, "quantity": quantity}
        else:
            self.inventory[category] = {product_name: {"price": price, "quantity": quantity}}
    def remove_product(self, category, product_name):
        if category in self.inventory and product_name in self.inventory[category]:
            del self.inventory[category][product_name]
    def update_product_quantity(self, category, product_name, quantity):
        if category in self.inventory and product_name in self.inventory[category]:
            self.inventory[category][product_name]["quantity"]= quantity
cart1 = Cart()
cart2 = Cart()
cart1.add_product("fruits", "mangoes", 3, 40)
cart2.add_product("vegitables", "sukuma", 20, 2)
cart2.add_product("vegitable", "cabbage", 10, 6)
cart2.remove_product("vegetables", "Kales")
cart2.update_product_quantity("vegitables", "sukuma", 4)
print(cart1.inventory)
print(cart2.inventory)



