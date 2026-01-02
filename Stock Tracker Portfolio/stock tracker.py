stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

total_investment = 0

file = open("portfolio.txt", "w")

print("Available stocks:", ", ".join(stocks.keys()))

while True:
    stock_name = input("Enter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        price = stocks[stock_name]
        value = price * quantity
        total_investment += value

        file.write(f"{stock_name} - Quantity: {quantity}, Value: {value}\n")
    else:
        print("Stock not available!")

file.write(f"\nTotal Investment Value: {total_investment}")
file.close()

print("Total Investment Value:", total_investment)
print("Portfolio saved to portfolio.txt")
