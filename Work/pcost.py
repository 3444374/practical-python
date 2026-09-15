# pcost.py
#
# Exercise 1.27
total_cost = 0

with open('./Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        price = float(row[2])
        shares = int(row[1])
        total_cost += shares*price

print('Total cost is', total_cost)