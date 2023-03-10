def verifier_triangle(*args):
    if len(args) == 3:
        a, b, c = args
        print("c'est un triangle")
        if a == b and b == c and a == c:
            return "c'est un triangle equilatéral"
        elif a == b or b == c or a == c:
            return "triangle isocèle"
        else:
            return "Triangle scalène"
    else:
            return "ce n'est pas un triangle"
print(verifier_triangle(3, 3, 9))