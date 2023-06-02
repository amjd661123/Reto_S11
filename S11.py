from llenado import llenar
from eliminar import eliminar

num = int(input("¿Cuántas listas quieres manejar?: "))

listas = []

for i in range(0,num):
    listas.append(llenar(int(input(f"Ingresa la lingitud de la lista {i+1}:"))))
print(listas)


eliminar(listas,0)