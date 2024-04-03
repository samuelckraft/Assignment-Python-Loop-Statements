#Task 1
x = 10
y = 5

iterations = 4
while x > y:
    x += 1
    iterations -= 1
    print("X is greater than Y")
    if iterations == 0:
        break

#Task 2
while x > y:
    x += 1
    print("X is greater than Y")
    if x > 14:
        break