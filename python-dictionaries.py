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
Question 2. Python Programming Challenges for Customer Service Data Handling

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


def new_service_ticket(tickets, ticket_num, customer, issue):
    new_ticket = "Ticket" + ticket_num
    if new_ticket in tickets:
        print(f"{new_ticket} already exists in our system.")
    else:
        tickets[new_ticket] = {"Customer": customer, "Issue": str.capitalize(issue), "Status": "open"}
        print(f"'{new_ticket}' has been added for '{customer}' with the issue '{str.capitalize(issue)}'")


def update_status(tickets, ticket_num, status):
    new_ticket = "Ticket"+ticket_num
    if new_ticket in tickets:
        tickets[new_ticket]["Status"] = status
        print(f"Ticket{new_ticket} status updated to {status}.")
    else:
        print(f"{new_ticket} doesn't exist.")


def display_tickets(tickets, choice = None):
    if choice:
        filtered_tickets = {id: ticket for id, ticket in tickets.item() if ticket['Status'] == choice}
        if filtered_tickets:
            for id, ticket in filtered_tickets.items():
                print(f"{id}: Customer: {ticket['Customer']}, Issue: {ticket['Issue']}")
        else:
            print(f"No tickets found with status '{choice}'.")
    else:
        print("All tickets:")
        for id, ticket in tickets.items():
            print(f"{id}: Customer: {ticket['Customer']}, Issue: {ticket['Issue']}, Status: {ticket['Status']}")
    


while True:
    print("-----------------------------------------")
    print("Ticket Menu:")
    print("-----------------------------------------")
    print("1. Open a new service ticket.")
    print("2. Update status.")
    print("3. Display tickets or filter by status.")
    print("4. Exit.")
    user_input = input("Please select one of our menu options: ")
    if user_input == "1":
        user_input1 = input("Please Enter ticket number: ")
        user_input2 = input("Customers name: ").title()
        user_input3 = input("Customers Issue: ")
        new_service_ticket(service_tickets, user_input1, user_input2, user_input3)
    elif user_input == "2":
        user_input1 = input("Please enter ticket number: ")
        user_input2 = input("What do you want to change status to: [OPEN/CLOSED] ").lower()
        update_status(service_tickets, user_input1, user_input2)
    elif user_input == "3":
        user_input1 = input("Open, Closed or Press Enter for all: ").lower()
        display_tickets(service_tickets, user_input1)
    elif user_input == "4":
        print("Thank you for using Service Ticket Handling Program")
        break
    else:
        print("Invalid input try again")