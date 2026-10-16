
# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0
portfolio = []

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found! Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity
    total_investment += investment

    portfolio.append({
        "Stock": stock_name,
        "Quantity": quantity,
        "Price": price,
        "Investment": investment
    })

    print("Investment added:", investment)

# Display portfolio
print("\n=== YOUR PORTFOLIO ===")

for stock in portfolio:
    print(
        stock["Stock"],
        "| Quantity:", stock["Quantity"],
        "| Price:", stock["Price"],
        "| Total:", stock["Investment"]
    )

print("\nTotal Investment =", total_investment)

# Save results to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("=======================\n")

    for stock in portfolio:
        file.write(
            f'{stock["Stock"]}, Quantity: {stock["Quantity"]}, '
            f'Price: {stock["Price"]}, '
            f'Investment: {stock["Investment"]}\n'
        )

    file.write(f"\nTotal Investment: {total_investment}\n")

print("Portfolio saved to portfolio.txt")
