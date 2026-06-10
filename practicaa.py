# Así de fácil se crea una lista con elementos en Python
inventario = ["Poción de Vida", "Escudo de Madera", "Espada Oxidada", "Antídoto"]

print("--- Revisando tu mochila ---")

# El bucle 'for' en Python lee directamente los elementos de la lista
for objeto in inventario:
    print(f"🎒 Tienes un objeto equipado: {objeto}")
    if "Espada Oxidada" in objeto:
        print("⚠️ ¡Esta arma necesita reparación!")
print("-------------------------------------")

# Las listas en Python tienen superpoderes. Añadamos un objeto nuevo:
print("¡Encontraste dos tesoros!")
inventario.append("Gemas de Oro") # '.append()' mete un elemento al final de la lista
inventario.append("Armadura de Cuero")

print(f"Tu inventario actualizado tiene {len(inventario)} objetos.") 
# 'len()' te dice el tamaño de la lista (como el .Length o .Count de C#)
print(inventario)

