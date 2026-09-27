import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 145,
    "MSFT": 330,
    "NFLX": 610,
}


def show_available_stocks():
    print("\nAvailable stocks and prices (per share):")
    for symbol, price in STOCK_PRICES.items():
        print(f"  {symbol:<6} ${price}")
    print()


def get_portfolio():
    portfolio = {}
    show_available_stocks()

    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' not found in price list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity of {symbol}: ").strip())
            if quantity < 0:
                print("  Quantity cannot be negative.\n")
                continue
        except ValueError:
            print("  Invalid number. Try again.\n")
            continue

        portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        print(f"  Added: {quantity} share(s) of {symbol}\n")

    return portfolio


def calculate_investment(portfolio):
    rows = []
    total = 0
    for symbol, quantity in portfolio.items():
        price = STOCK_PRICES[symbol]
        subtotal = price * quantity
        rows.append((symbol, quantity, price, subtotal))
        total += subtotal
    return rows, total


def display_summary(rows, total):
    print("\n" + "=" * 45)
    print("PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Subtotal':<12}")
    print("-" * 45)
    for symbol, quantity, price, subtotal in rows:
        print(f"{symbol:<8}{quantity:<8}${price:<9}${subtotal:<11}")
    print("-" * 45)
    print(f"TOTAL INVESTMENT: ${total}")
    print("=" * 45 + "\n")


def save_to_file(rows, total):
    choice = input("Save results to a file? (txt / csv / no): ").strip().lower()

    if choice not in ("txt", "csv"):
        print("Skipping file save.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"portfolio_summary_{timestamp}.{choice}"

    if choice == "txt":
        with open(filename, "w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write(f"{'Symbol':<8}{'Qty':<8}{'Price':<10}{'Subtotal':<12}\n")
            for symbol, quantity, price, subtotal in rows:
                f.write(f"{symbol:<8}{quantity:<8}${price:<9}${subtotal:<11}\n")
            f.write(f"\nTOTAL INVESTMENT: ${total}\n")
    else:  # csv
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Symbol", "Quantity", "Price", "Subtotal"])
            for row in rows:
                writer.writerow(row)
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total])

    print(f"Results saved to '{filename}'\n")


def main():
    print("=== Stock Portfolio Tracker ===")
    portfolio = get_portfolio()

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    rows, total = calculate_investment(portfolio)
    display_summary(rows, total)
    save_to_file(rows, total)


if __name__ == "__main__":
    main()