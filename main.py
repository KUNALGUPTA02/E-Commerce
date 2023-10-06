from product import Laptop, Headphones
from discount import PercentageDiscount
from cart import Cart, ShoppingCart


laptop = Laptop("Laptop", 1000, True)
headphones = Headphones("Headphones", 50, True)

if __name__ == "__main__":
    print("Available products:")
    print("1. Laptop - $1000")
    print("2. Headphones - $50")

    # Initialize products
    laptop = Laptop("Laptop".lower(), 1000, True)
    headphones = Headphones("Headphones".lower(), 50, True)

    # cart
    cart = Cart()

    while True:
        print("\nOptions:")
        print("1. Add a product to the cart")
        print("2. View cart")
        print("3. Update quantity by adding or removing")
        print("4. Calculate total bill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            product = input(
                "Enter the product name (Laptop/Headphones): ")
            quantity = int(input("Enter the quantity: "))
            if product.lower() == "laptop":
                cart.add_to_cart(laptop, quantity)
            elif product.lower() == "headphones":
                cart.add_to_cart(headphones, quantity)
            else:
                print("Invalid product choice. Please try again.")

        elif choice == "2":
            print(
                "Cart Items:", f"You have {sum(1 for item in cart.cart_items if item.name=='laptop')} Laptops and {sum(1 for item in cart.cart_items if item.name=='headphones')} Headphones in your cart.")

        elif choice == "3":
            update = input("What you want add or remove ?: ")
            if update.lower() == "add":
                product = input(
                    "Enter the product name which you want to add : ")
                quantity = int(input("Enter the quantity: "))
                if product.lower() == "laptop":
                    cart.update_quantity(laptop, quantity)
                elif product.lower() == "headphones":
                    cart.update_quantity(headphones, quantity)
                else:
                    print("Invalid product choice. Please try again.")
            elif update.lower() == "remove":
                product = input(
                    "Enter the product name which you want to remove : ")
                quantity = int(input("Enter the quantity to delete: "))
                if product.lower() == "laptop":
                
                    cart.remove_from_cart(laptop, quantity)
                elif product.lower() == "headphones":
                    cart.remove_from_cart(headphones, quantity)
                else:
                    print("Invalid product choice. Please try again.")

        elif choice == "4":
            discount_choice = input(
                "Apply a discount? (y/n): ").strip().lower()
            if discount_choice == "y":
                discount_percentage = input(
                    "Enter the discount percentage: ").strip()
                try:
                    discount_percentage = float(discount_percentage)
                except ValueError:
                    print("Invalid discount percentage. Please enter a valid number.")
                    continue

                shopping_cart = ShoppingCart(
                    PercentageDiscount(discount_percentage))
            else:
                shopping_cart = ShoppingCart()

            shopping_cart.cart = cart
            total_bill = shopping_cart.calculate_total_bill()
            print(f"Total Bill: Your total bill is ${total_bill}.")
        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")
