# run using python Python\ Distilled/chapter_1/pcost.py "Python Distilled/data/portfolio.csv"
import sys
from pprint import pprint

if len(sys.argv) != 2:
    raise SystemExit(f"Usage: {sys.argv[0]} <filename>")

rows = []
with open(sys.argv[1], "r") as file:
    while (line := file.readline()):
        rows.append(line.strip().split(","))

print(f"Extracted {len(rows)} rows from {sys.argv[1]}:")
print(f"{'Name': >8} {'Shares': >8} {'Price': >6}")
pprint(rows[:10], indent=2)  # Print the first 10 rows as a sample

total_value = sum(int(shares) * float(price) for _, shares, price in rows)

# or you can clean the data first and then calculate the total value
cleaned_rows = []
for name, shares, price in rows:
    try:
        shares = int(shares)
        price = float(price)
        cleaned_rows.append((name, shares, price))
    except ValueError as e:
        print(f"Error converting shares or price for {name}: {e}")
total_value = sum(shares * price for _, shares, price in cleaned_rows)
        
print(f"\nTotal value of the portfolio: ${total_value:.2f}")

holdings = {name for name, _, _ in cleaned_rows}
print(f"\nUnique holdings object type: {type(holdings)}")
print(f"\nUnique holdings in the portfolio: {holdings}")

holdings_lookup = {s[0]: (s[1], s[2]) for s in cleaned_rows}
print(f"\nHoldings lookup object type: {type(holdings_lookup)}")
print(f"Holdings lookup dictionary:")
pprint(holdings_lookup, indent=2)
