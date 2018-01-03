limit = 1000
sum = 0
i = 1

while i < limit:
    if i % 3 == 0 or i % 5 == 0:
        sum += i

    i += 1

print(sum)
