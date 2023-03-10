# somme = 4
# divisible = 1
# count = 0
# while divisible <= somme:
#     if somme % divisible == 0:
#         count += 1
#     divisible += 1
# print(count)


# Départ = 1

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

