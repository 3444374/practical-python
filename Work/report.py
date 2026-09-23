# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            temp = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
            portfolio.append(temp)

    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except (IndexError):
                # print(f"Invalid price data: {row}")
                continue

    return prices

if __name__ == '__main__':
    portfolio = read_portfolio('./Data/portfolio.csv')
    prices = read_prices('./Data/prices.csv')
    # print(portfolio)
    # print(prices)