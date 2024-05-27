number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Error: Invalid number of items!")
    number_of_items = int(input("Number of items: "))
totalPrices = float()
for i in range(1, number_of_items + 1, 1):
    price = float(input("Price of item: "))
    totalPrices += price

if totalPrices > 100:
    totalPrices = (totalPrices / 100) * 90
else:
    totalPrices = totalPrices

print(f"Total price for {number_of_items} items is ${totalPrices:.2f}")
