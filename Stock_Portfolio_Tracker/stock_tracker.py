stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300
}

total_investment = 0

print("Available Stocks:")
for stock, price in stocks.items():
    print(f"{stock}: ${price}")

while True:
    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter quantity: "))
        total_investment += stocks[stock_name] * quantity
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total_investment}")

print("Result saved in portfolio.txt")