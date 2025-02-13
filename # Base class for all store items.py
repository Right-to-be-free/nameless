# Base class for all store items
class Product:
    def __init__(self, name, price, quantity):
        """Constructor to initialize product details"""
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def update_stock(self, amount):
        """Method to update stock quantity"""
        self.quantity += amount
        return f"Updated stock for {self.name}. New quantity: {self.quantity}"
    
    def sell(self, amount):
        """Method to sell an item and reduce stock"""
        if amount > self.quantity:
            return f"Not enough stock for {self.name}!"
        self.quantity -= amount
        return f"Sold {amount} {self.name}(s). Remaining: {self.quantity}"
    
    def __del__(self):
        """Destructor to delete object when no longer needed"""
        print(f"{self.name} is removed from inventory.")


# Derived class for Perishable Items (Inheritance)
class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_date):
        """Constructor for perishable items"""
        super().__init__(name, price, quantity)
        self.expiry_date = expiry_date
    
    def check_expiry(self):
        """Method to check expiry date"""
        return f"{self.name} expires on {self.expiry_date}"


# Store Class (Encapsulation: Managing Store Inventory)
class GroceryStore:
    def __init__(self, store_name, *products):
        """Constructor using *args to accept multiple products"""
        self.store_name = store_name
        self.inventory = {product.name: product for product in products}
    
    def add_product(self, product):
        """Method to add a new product to inventory"""
        self.inventory[product.name] = product
        return f"Added {product.name} to the inventory."
    
    def get_product(self, name):
        """Method to retrieve a product from inventory"""
        return self.inventory.get(name, "Product not found")

    def show_inventory(self):
        """Method to display inventory"""
        return {name: product.quantity for name, product in self.inventory.items()}
    
    def sell_product(self, name, quantity):
        """Method to sell a product"""
        product = self.get_product(name)
        if isinstance(product, Product):
            return product.sell(quantity)
        return "Product not found"


# Using Polymorphism with method overloading using *args and **kwargs
class Discount:
    def apply_discount(self, product, *args, **kwargs):
        """Apply discount based on parameters"""
        if args:
            discount = args[0]
            product.price -= product.price * (discount / 100)
        elif "fixed_amount" in kwargs:
            product.price -= kwargs["fixed_amount"]
        return f"New price of {product.name} is {product.price}"


# Example Usage
if __name__ == "__main__":
    # Creating product instances
    rice = Product("Rice", 50, 100)
    milk = PerishableProduct("Milk", 20, 50, "2025-03-10")
    
   
