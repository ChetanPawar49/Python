class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def reduce_stock(self, quantity):
        if quantity <= self.stock_quantity:
            self.stock_quantity -= quantity
        else:
            raise ValueError("Not enough stock available")

    def __str__(self):
        return f"{self.name} - Price: {self.price}, Stock: {self.stock_quantity}"

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name}: {self.quantity} @ {self.product.price} each"

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.stock_quantity >= quantity:
            self.items.append(CartItem(product, quantity))
        else:
            print(f"Cannot add {quantity} of {product.name}. Only {product.stock_quantity} in stock.")

    def remove_product(self, product_name):
        for item in self.items:
            if item.product.name == product_name:
                self.items.remove(item)
                print(f"{product_name} removed from cart.")
                return
        print(f"{product_name} not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
        else:
            for item in self.items:
                print(item)
            print(f"Total Price: {self.calculate_total()}")

    def calculate_total(self):
        return sum(item.get_total_price() for item in self.items)

    def checkout(self):
        total_price = self.calculate_total()
        for item in self.items:
            try:
                item.product.reduce_stock(item.quantity)
            except ValueError as e:
                print(e)
                return
        print(f"Checkout successful! Total price: {total_price}")
        self.items = []  # Clear the cart after checkout

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = ShoppingCart()

    def add_to_cart(self, product, quantity):
        self.cart.add_product(product, quantity)

    def remove_from_cart(self, product_name):
        self.cart.remove_product(product_name)

    def view_cart(self):
        self.cart.view_cart()

    def checkout(self):
        self.cart.checkout()

# Example Usage:
# Products
p1 = Product("Laptop", 1000, 5)
p2 = Product("Headphones", 200, 10)
p3 = Product("Keyboard", 150, 2)

# User
user = User("chetan", "password123")

# Adding products to the cart
user.add_to_cart(p1, 1)
user.add_to_cart(p2, 2)
user.add_to_cart(p3, 3)  # This should raise an error due to insufficient stock

# Viewing cart
user.view_cart()

# Removing a product
user.remove_from_cart("Headphones")

# Viewing cart after removal
user.view_cart()

# Checkout
user.checkout()

# Viewing cart after checkout
user.view_cart()