print("Bienvenido al cotizador de viajes ExploraBoyacá")
print("----------------------------------------------")

# Precios base por destino (por persona por día)
destinos = {
    "Villa de Leyva": 180000,
    "Lago de Tota": 200000,
    "Puente de Boyacá": 150000,
    "Ráquira": 160000,
    "Sierra Nevada del Cocuy": 250000
}

# Mostrar destinos disponibles
print("\nDestinos disponibles:")
for destino in destinos:
    print(f"- {destino}")

# Solicitar datos al usuario
destino = input("\nElige un destino: ")
while destino not in destinos:
    print("Destino no válido. Por favor elige uno de la lista.")
    destino = input("Elige un destino: ")

personas = int(input("Número de personas: "))
while personas <= 0:
    print("El número de personas debe ser mayor a 0.")
    personas = int(input("Número de personas: "))

dias = int(input("Cantidad de días: "))
while dias <= 0:
    print("La cantidad de días debe ser mayor a 0.")
    dias = int(input("Cantidad de días: "))

# Calcular costo total
precio_base = destinos[destino]
total = precio_base * personas * dias

# Mostrar resultado
print("\n--- Resumen de cotización ---")
print(f"Destino: {destino}")
print(f"Personas: {personas}")
print(f"Días: {dias}")
print(f"Precio por persona por día: ${precio_base:,}")
print(f"Total estimado: ${total:,}")

print("\n¡Gracias por usar nuestro cotizador!")