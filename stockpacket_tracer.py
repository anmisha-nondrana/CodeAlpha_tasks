import csv
from datetime import datetime


STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOG": 140.00,
    "AMZN": 145.00,
    "MSFT": 330.00,
    "NFLX": 610.00,
}

def show_available_stocks():
    """Display all available stocks and their prices."""

    print("\n" + "=" * 45)
    print("AVAILABLE STOCKS")
    print("=" * 45)

    print(f"{'Symbol':<12}{'Price':>15}")
    print("-" * 45)

    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<12}${price:>14.2f}")

    print("=" * 45)


def display_menu():
    """Display the main application menu."""

    print("\n" + "=" * 45)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 45)
    print("1. View available stocks")
    print("2. Add stock to portfolio")
    print("3. View portfolio")
    print("4. Remove stock from portfolio")
    print("5. Save portfolio")
    print("6. Exit")
    print("=" * 45)


def get_stock_symbol():
    """Ask the user for a valid stock symbol."""

    while True:
        symbol = input("Enter stock symbol: ").strip().upper()

        if symbol in STOCK_PRICES:
            return symbol

        print("Invalid stock symbol.")
        print("Please choose a symbol from the available stocks.\n")


def get_quantity():
    """Ask the user for a valid positive quantity."""

    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue

            return quantity

        except ValueError:
            print("Please enter a valid whole number.")


def add_stock(portfolio):
    """Add shares of a stock to the portfolio."""

    show_available_stocks()

    symbol = get_stock_symbol()
    quantity = get_quantity()

    portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    print(
        f"\nAdded {quantity} share(s) of {symbol} "
        f"to your portfolio."
    )


def remove_stock(portfolio):
    """Remove shares of a stock from the portfolio."""

    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    display_portfolio(portfolio)

    symbol = input(
        "\nEnter the stock symbol to remove: "
    ).strip().upper()

    if symbol not in portfolio:
        print(f"{symbol} is not in your portfolio.")
        return

    try:
        quantity = int(
            input("Enter quantity to remove: ")
        )

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > portfolio[symbol]:
            print(
                f"You only own {portfolio[symbol]} "
                f"share(s) of {symbol}."
            )
            return

        portfolio[symbol] -= quantity

        if portfolio[symbol] == 0:
            del portfolio[symbol]

        print(
            f"Removed {quantity} share(s) of {symbol}."
        )

    except ValueError:
        print("Please enter a valid whole number.")


def calculate_portfolio(portfolio):
    """
    Calculate portfolio rows and total investment.

    Returns:
        rows: list of stock calculation details
        total: total portfolio value
    """

    rows = []
    total = 0

    for symbol, quantity in portfolio.items():

        price = STOCK_PRICES[symbol]
        subtotal = price * quantity

        rows.append({
            "symbol": symbol,
            "quantity": quantity,
            "price": price,
            "subtotal": subtotal
        })

        total += subtotal

    return rows, total


def display_portfolio(portfolio):
    """Display the current portfolio."""

    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    rows, total = calculate_portfolio(portfolio)

    print("\n" + "=" * 60)
    print("                 PORTFOLIO SUMMARY")
    print("=" * 60)

    print(
        f"{'Symbol':<10}"
        f"{'Quantity':<12}"
        f"{'Price':<15}"
        f"{'Value':<15}"
    )

    print("-" * 60)

    for row in rows:
        print(
            f"{row['symbol']:<10}"
            f"{row['quantity']:<12}"
            f"${row['price']:<14.2f}"
            f"${row['subtotal']:<14.2f}"
        )

    print("-" * 60)
    print(f"{'TOTAL INVESTMENT':<37}${total:.2f}")
    print("=" * 60)


def display_statistics(portfolio):
    """Display basic portfolio statistics."""

    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    rows, total = calculate_portfolio(portfolio)

    total_shares = sum(
        row["quantity"] for row in rows
    )

    highest_value_stock = max(
        rows,
        key=lambda row: row["subtotal"]
    )

    print("\n" + "=" * 45)
    print("PORTFOLIO STATISTICS")
    print("=" * 45)

    print(f"Number of stocks: {len(rows)}")
    print(f"Total shares: {total_shares}")
    print(f"Total investment: ${total:.2f}")

    print(
        f"Largest position: "
        f"{highest_value_stock['symbol']} "
        f"(${highest_value_stock['subtotal']:.2f})"
    )

    print("=" * 45)


def save_as_txt(rows, total, filename):
    """Save portfolio information as a TXT file."""

    with open(filename, "w", encoding="utf-8") as file:

        file.write("STOCK PORTFOLIO SUMMARY\n")
        file.write("=" * 60 + "\n\n")

        file.write(
            f"{'Symbol':<10}"
            f"{'Quantity':<12}"
            f"{'Price':<15}"
            f"{'Value':<15}\n"
        )

        file.write("-" * 60 + "\n")

        for row in rows:
            file.write(
                f"{row['symbol']:<10}"
                f"{row['quantity']:<12}"
                f"${row['price']:<14.2f}"
                f"${row['subtotal']:<14.2f}\n"
            )

        file.write("-" * 60 + "\n")
        file.write(f"TOTAL INVESTMENT: ${total:.2f}\n")


def save_as_csv(rows, total, filename):
    """Save portfolio information as a CSV file."""

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Symbol",
            "Quantity",
            "Price",
            "Value"
        ])

        for row in rows:
            writer.writerow([
                row["symbol"],
                row["quantity"],
                f"{row['price']:.2f}",
                f"{row['subtotal']:.2f}"
            ])

        writer.writerow([])
        writer.writerow([
            "TOTAL INVESTMENT",
            "",
            "",
            f"{total:.2f}"
        ])


def save_portfolio(portfolio):
    """Save portfolio to TXT or CSV."""

    if not portfolio:
        print("\nYour portfolio is empty.")
        return

    rows, total = calculate_portfolio(portfolio)

    print("\nChoose file format:")
    print("1. TXT")
    print("2. CSV")
    print("3. Cancel")

    choice = input("Enter your choice: ").strip()

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    if choice == "1":

        filename = (
            f"portfolio_summary_{timestamp}.txt"
        )

        save_as_txt(rows, total, filename)

    elif choice == "2":

        filename = (
            f"portfolio_summary_{timestamp}.csv"
        )

        save_as_csv(rows, total, filename)

    elif choice == "3":

        print("Save cancelled.")
        return

    else:

        print("Invalid choice.")
        return

    print(f"\nPortfolio saved successfully:")
    print(filename)


def main():
    """Run the Stock Portfolio Tracker."""

    portfolio = {}

    print("\nWelcome to Stock Portfolio Tracker!")

    while True:

        display_menu()

        choice = input(
            "Enter your choice (1-6): "
        ).strip()

        if choice == "1":

            show_available_stocks()

        elif choice == "2":

            add_stock(portfolio)

        elif choice == "3":

            display_portfolio(portfolio)
            display_statistics(portfolio)

        elif choice == "4":

            remove_stock(portfolio)

        elif choice == "5":

            save_portfolio(portfolio)

        elif choice == "6":

            print("\nThank you for using")
            print("Stock Portfolio Tracker!")
            print("Goodbye!")
            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1-6."
            )

if __name__ == "__main__":
    main()