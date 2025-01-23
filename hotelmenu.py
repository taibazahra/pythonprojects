
menu = {
    'Pizza': 40,
    'pasta': 60,
    'Burger': 45,
    'coffee': 67,
    'salad': 90
}
#greetings
print("welcome to our restaurant")
print("Pizza: rs 40\n Pasta: 60\n Burger: 45\n coffee: 67\n salad: 90")
order_total = 0

item_1 = input("enter the name of the item =  ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has n=been added to your order")
else:
    print(f"ordered item {item_1} is not available")

another_order = input("do you want to add another item? ")
if another_order=="yes":
    item_2 = input("enter the name of second order: ")
    order_total += menu[item_2]
else:
    print("we are moving with current order")

print(f"the total amount is {order_total}")