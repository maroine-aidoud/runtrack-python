multiple_count = 0
L = [8, 24, 48, 2, 16]

for i in L:
    if i % 3 == 0:
        multiple_count += 1

print("count:", multiple_count )