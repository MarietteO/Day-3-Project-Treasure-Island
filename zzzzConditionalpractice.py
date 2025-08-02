amount = 0

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

size_options = {"s": 15, "m": 20, "l": 25}
pepperoni_options = {"s": 2, "m": 3, "l": 3}

amount += size_options[size]
if pepperoni == "y":
    amount += pepperoni_options[size]
if extra_cheese == "y":
    amount += 1

print(f"That will be R{amount}, please.")
