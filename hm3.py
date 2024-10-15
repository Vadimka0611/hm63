num = int(input("Write your number: "))

update = num

while update >= 10:
    count = 1
    for i in str(update):
        count *= int(i)

    update = count

print(update)