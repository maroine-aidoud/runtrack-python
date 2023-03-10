count = 0
i = 2


while i <= 1000:
    somme = 2
    divisible = 2
    
    while divisible <= somme:
        if somme % divisible == 0:
            break

        divisible += 1
        somme += i
    
    if somme == i * 2:
        count += 1
        print(i)

    i += 1


