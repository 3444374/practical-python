# report.py
#
# Exercise 2.4

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        header = next(f)
        for line in f:
            row = line.split(',')
            temp = {'name' : row[0], 'shares' : int(row[1]), 'price' : float(row[2])}
            portfolio.append(temp)

    return portfolio

if __name__ == '__main__':
    portfolio = read_portfolio('./Data/portfolio.csv')
    print(portfolio)