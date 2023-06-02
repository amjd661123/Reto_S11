def llenar(l):
    x = []
    for i in range(0,l):
        x.append(input(f"Elemento {i+1} de {l}: "))
    print(f"Lista final: {x}")
    return x