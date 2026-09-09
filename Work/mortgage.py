# mortgage.py
#
# Exercise 1.7
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
i = 0

while principal > 0:
    if i >= extra_payment_start_month - 1 and i < extra_payment_end_month: 
        payment = 2684.11 + extra_payment
    else: payment = 2684.11

    if principal * (1+rate/12) < payment:
        payment = principal * (1+rate/12)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    i = i + 1
    print(i, total_paid, principal)


    

print('Total paid', total_paid,'Demand months', i)
