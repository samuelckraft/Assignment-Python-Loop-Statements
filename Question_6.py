#Task 1
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

sliced = genres[1:4]

print(sliced)

#Task 2
for x in genres:
    print(f"{x} Music")

#Task 3
countdown = 10

for x in reversed(range(1,11)):
    while x > 0:
        print(x)
        x -= 1
    else:
        print("The beat drops now")
        break
    