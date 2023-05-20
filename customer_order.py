class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
class Recieved:
    def __init__(self, order_number, customer_name):
        self.order_number = order_number
        self.customer_name = customer_name
        self.items = []
    def add_item(self, product, quantity):
        self.items.append(OrderItem(product, quantity))
    def calculate_total_price(self):
        return sum(item.product.price * item.quantity for item in self.items)
class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.orders = []
    def place_order(self, order):
        self.orders.append(order)
    def get_order_by_number(self, order_number):
        return next((order for order in self.orders if order.order_number == order_number), None)
#instances
product1 = Product(1, "kales", 20)
order1 = Recieved(1, "Faith")
order1.add_item(product1, 5)
customer1 = Customer(1, "Lindsay")
customer1.place_order(order1)
found_order = customer1.get_order_by_number(1)
if found_order:
    print("Order found:")
    print("Order Number:", found_order.order_number)
    print("Customer Name:", found_order.customer_name)
    print("Total Price:", found_order.calculate_total_price())
else:
    print("Order not found.")












