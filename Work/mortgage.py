# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
i = 0

while principal > 0:
    if i < 12: 
        payment = 3684.11
    else: payment = 2684.11

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    i = i + 1

print('Total paid', total_paid,'Demand months', i + 1)
