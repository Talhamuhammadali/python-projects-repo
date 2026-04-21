"""Python comprehension with portfolio data."""

import sys
from pprint import pprint

if len(sys.argv) != 2:
    raise SystemExit(f"Usage: {sys.argv[0]} <filename>")
file_path = sys.argv[1]

with open(file_path, "r") as f:
    portfolio = [
        {
            "name": data[0], "shares": int(data[1]), "price": float(data[2])
        } 
        for item in f.readlines() if item for data in [item.split(",")]
    ]
    
    print("Portfolio:\n")
    pprint(portfolio, indent=2)
    names = {item["name"] for item in portfolio}
    print("\nNames:\n")
    pprint(names, indent=2)
    more100 = [item for item in portfolio if item["price"] > 100]
    print("\nMore than 100:\n")
    pprint(more100, indent=2)
    num_shares = [item["shares"] for item in portfolio]
    print("\nNumber of shares:\n")
    pprint(num_shares, indent=2)
    print(f"\nTotal shares:\n {sum(num_shares)}")
    