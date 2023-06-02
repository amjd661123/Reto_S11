def eliminar(listas, l):
    for i in range(0,len(listas)):
        if i != l:
            x = []
            for j in listas[i]:
                if j not in listas[l]:
                    x.append(j)
            print(f"Lista resultado de eliminar los elementos de la lista {i} en la lista {j}: {x}")