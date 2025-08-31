# Hardcoded stock prices (dictionary)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "MSFT": 320,
    "AMZN": 140
}

portfolio = {}  # to store user's chosen stocks and quantities

print("Welcome to Stock Portfolio Tracker")
print("Available stock prices: ")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

#  User input loop ------------

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Stock not found! Please choose from the list above.")
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock_name}: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            continue

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    except ValueError: 
        print("Please enter a valid number.")

# Calculate Total Investment -----------

total_investment = 0
print("\n Portfolio Summary: ")
print("{:<10} {:<10} {:<10} {:<10}".format("Stock", "Quantity", "Price", "Investment"))
print("-" * 50)

for stock, qty in portfolio.items():
    investment = stock_prices[stock] * qty
    total_investment += investment
    print("{:<10} {:<10} ${:<9} ${:<10}".format(stock, qty, stock_prices[stock], investment))
    #print(f"{stock}: {qty} * ${stock_prices[stock]} = ${investment}")

print("-" * 50)
print(f"{'TOTAL':<10} {'':<10} {'':<10} ${total_investment}")
#print("\nTotal Investment Value: $", total_investment)

# Save to File -------

choice = input("\nDo you want to save portfolio to a file? (y/n): ").lower()
if choice == "y":
    file_type = input("Save as TXT or CSV? (txt/csv): ").lower()

    if file_type == "txt":
        with open("/home/neetu/Documents/Intership/CodeAlpha_Internship/CodeAlpha_StockPortfolioTracker/portfolio.txt", "w") as f:
            f.write("Portfolio Summary : \n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} * ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")

            f.write(f"\nTotal Investment Value: ${total_investment}")
        
        print("Saved as portfolio.txt")

    elif file_type == "csv":
        import csv
        with open("/home/neetu/Documents/Intership/CodeAlpha_Internship/CodeAlpha_StockPortfolioTracker/portfolio.csv", "w", newline="") as f:
            #writer = csv.DictWriter(f)
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Investment"])

            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])

            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total_investment])

        print("Saved as portfolio.csv")