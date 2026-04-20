# Sistema de descuentos para videojuegos

precio = float(input("Ingrese el precio del videojuego: Q"))
vip = input("¿El cliente es miembro VIP? (Sí/No): ").strip().lower()

if precio >= 500:
    precio = precio * 0.90  # descuento del 10%

if vip == "sí" or vip == "si":
    precio = precio * 0.85  # descuento del 15%

print(f"El precio final que debe pagar el cliente es: Q{precio:.2f}")
