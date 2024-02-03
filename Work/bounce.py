# bounce.py
#
# Exercise 1.5

height = 100
bounce = 3 / 5
num = 0

while num < 10:
    bounce_height = height * bounce
    height = bounce_height
    num += 1
    print(num, round(bounce_height, 4))
