# mortgage.py
#
# Exercise 1.7

# principal = 500000
# rate = 0.05
# time_period = 30
# amount = 2684.11
# total_amount = 0


# while principal > 0:
#     principal = principal * (1 + rate / 12) - amount
#     total_amount += amount

# print("Total amount paid: ", round(total_amount, 1))


principal = 500000
rate = 0.05
time_period = 360
amount = 2684.11
total_amount = 0
t = 1

while principal > 0:
    if t <= 12:
        fixed_amount = 1000
        principal = principal * (1 + rate / 12) - (amount + fixed_amount)
        total_amount += amount + fixed_amount
        t += 1

    elif t < time_period and t > 12:
        principal = principal * (1 + rate / 12) - amount
        total_amount += amount
        t += 1

print(f"Total amount paid: {total_amount}")
print(f"Total months taken: {t}")
