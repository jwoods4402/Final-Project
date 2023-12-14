class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = int(quantity)
        self.calories = 0  
        self.fat = 0.0  
        self.cholesterol = 0  

class Grocery:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingList:
    def __init__(self):
        self.products = []
        self.groceries = []

    def add_product(self, product):
        self.products.append(product)

    def add_grocery(self, grocery):
        self.groceries.append(grocery)

    def display_product_info(self, product):
        print(f"Product: {product.name}")
        print(f"Quantity: {product.quantity}")
        print(f"Calories: {product.calories}")
        print(f"Fat: {product.fat}g")
        print(f"Cholesterol: {product.cholesterol}mg")
        print()

    def display_total_nutrients(self):
        total_calories = sum(product.calories * product.quantity for product in self.products)
        total_fat = sum(product.fat * product.quantity for product in self.products)
        total_cholesterol = sum(product.cholesterol * product.quantity for product in self.products)

        print("Total Nutrient Content:")
        print(f"Total Calories: {total_calories}")
        print(f"Total Fat: {total_fat}g")
        print(f"Total Cholesterol: {total_cholesterol}mg")

    def display_grocery_info(self, grocery):
        print(f"Grocery: {grocery.name}")
        print(f"Price: ${grocery.price:.2f}")
        print()

    def display_total_expenses(self):
        total_expenses = sum(item.price for item in self.groceries)
        print("Total Expenses:")
        print(f"Total Grocery Expenses: ${total_expenses:.2f}")

if __name__ == "__main__":
    shopping_list = ShoppingList()

    while True:
        category = input("Enter the category (product/grocery) or 'done' to finish: ")
        if category.lower() == 'done':
            break

        name = input("Enter the name: ")
        if category.lower() == 'product':
            quantity = input("Enter the quantity: ")
            try:
                quantity = int(quantity)
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")
                continue
            item = Product(name, quantity)
            shopping_list.add_product(item)
        elif category.lower() == 'grocery':
            try:
                price = float(input("Enter the price: $"))
            except ValueError:
                print("Invalid input. Please enter a valid price.")
                continue
            item = Grocery(name, price)
            shopping_list.add_grocery(item)
        else:
            print("Invalid category. Please enter 'product' or 'grocery'.")

    for product in shopping_list.products:
        shopping_list.display_product_info(product)

    for grocery in shopping_list.groceries:
        shopping_list.display_grocery_info(grocery)

    shopping_list.display_total_nutrients()
    shopping_list.display_total_expenses()