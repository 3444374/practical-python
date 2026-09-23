# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(header, row))
            try:
                temp = {'name' : record['name'], 'shares' : int(record['shares']), 'price' : float(record['price'])}
                portfolio.append(temp)
            except (ValueError, IndexError):
                print(f"Row {rowno}: Bad row: {row}")
                continue

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

def make_report(portfolio, prices):
    '''
    Generate a report as a list of tuples (name, shares, price, change)
    '''
    report = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        current_price = prices[name]
        change = current_price - stock['price']
        report.append((name, shares, current_price, change))

    return report


if __name__ == '__main__':
    portfolio = read_portfolio('./Data/portfolio.csv')
    prices = read_prices('./Data/prices.csv')
    report = make_report(portfolio, prices)
    print(portfolio)
    # print(prices)
    headers = ('Name', 'Shares', 'Price', 'Change')
    seperator = '----------'
    print('%10s %10s %10s %10s' % headers)
    print('%10s %10s %10s %10s' % (seperator, seperator, seperator, seperator))
    for r in report:
        print('%10s %10d %10.2f %10.2f' % r)