
inventario = ["Poción de Vida", "Escudo de Madera", "Espada Oxidada", "Antídoto"]

print("--- Revisando tu mochila ---")


for objeto in inventario:
    print(f"🎒 Tienes un objeto equipado: {objeto}")
    if "Espada Oxidada" in objeto:
        print("⚠️ ¡Esta arma necesita reparación!")
print("-------------------------------------")


print("¡Encontraste dos tesoros!")
inventario.append("Gemas de Oro") 
inventario.append("Armadura de Cuero")
inventario.append("Casco de Cuero")

print(f"Tu inventario actualizado tiene {len(inventario)} objetos.") 
print(inventario)

