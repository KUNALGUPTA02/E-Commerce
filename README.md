# E-Commerce-

## Problem Statement
### Develop a simple E-commerce cart system where users can add products to their cart, update quantities, and view the total bill. Products should have attributes like name, price, and availability status.
- Functional Requirements
1. Display a list of products with their attributes.
2. Allow users to add products to the cart.
3. Implement cart functionality where users can view, update quantities, and remove items.
4. Calculate and display the total bill.

   
## Key Focus
1. Behavioral Pattern: Use Strategy Pattern to handle different discount strategies, like percentage off or buy one get one free.
2. Creational Pattern: Use Prototype Pattern to clone product objects when adding to the cart.
3. OOP: Emphasize encapsulation and inheritance. For instance, create a base 'Product' class and specialized subclasses for different types of products.

## Usage
1.clone the repositorites.
https://github.com/KUNALGUPTA02/E-Commerce--Educational-Initiatives-.git
```sh
cd E-Commerce-main
```
2.Run the Application.
```sh
python main.py
```




## Possible Inputs
- Products: [{name: "Laptop", price: 1000, available: true}, {name: "Headphones", price: 50, available: true}]
- Add to Cart: "Laptop"
- Update Quantity: "Laptop, 2"
- Remove from Cart: "Headphones"

## Possible Outputs
- Cart Items: "You have 2 Laptops and 1 Headphone in your cart."
- Total Bill: "Your total bill is $2050."
