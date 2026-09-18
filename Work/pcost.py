# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            price = float(row[2])
            shares = int(row[1])
            total_cost += shares*price

    return total_cost

if __name__ == "__main__":
    cost = portfolio_cost('./Data/portfolio.csv')
    print(cost)