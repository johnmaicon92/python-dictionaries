"""
Question 1. Real-World Python Dictionary Applications
Objective: The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods.

Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions

Problem Statement: Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
- Add a new category called "Beverages" with at least two items.

- Update the price of "Steak" to 17.99.

- Remove "Bruschetta" from "Starters".
"""

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Sparkling Water": 1.19, "Orange Juice": 3.15, "Red Wine": 9.99}
restaurant_menu["Main Course"]["Steak"] = 17.99
removed_item = restaurant_menu["Starters"].pop("Bruschetta")
print(restaurant_menu)


"""
2. Python Programming Challenges for Customer Service Data Handling
Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
-Open a new service ticket.
-Update the status of an existing ticket.
-Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.
Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.
"""

service_tickets = {
    "Ticket1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}


def new_service_ticket():
    number = int(input("Please enter the number of the new ticket: "))
    print(f"Ticket{number}:")
new_service_ticket()


def update_status():
    pass


def display_tickets():
    for ticket in service_tickets:
        print(f"{ticket}: Customer - {service_tickets[ticket]['Customer']}, Issue - {service_tickets[ticket]['Issue']}, Status - {service_tickets[ticket]['Status']}")
display_tickets()