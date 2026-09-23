# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers, row))
            try:
                price = float(record['price'])
                shares = int(record['shares'])
                total_cost += shares*price
            except (ValueError, IndexError):
                print(f"Row {rowno}: Bad row: {row}")
                continue

    return total_cost

if __name__ == "__main__":
    cost = portfolio_cost('./Data/portfolio.csv')
    cost2 = portfolio_cost('./Data/portfoliodate.csv')
    # print(cost)
    print(cost2)