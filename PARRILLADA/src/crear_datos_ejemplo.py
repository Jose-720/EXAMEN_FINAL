# Ejemplo de script para llenar archivos de datos con datos de ejemplo

import os
import json

# Obtener la ruta del directorio actual
directorio_actual = os.path.dirname(__file__)

# Datos de ejemplo para ventas
ventas_ejemplo = [
    {"comprador": "Juan", "evento": "Parrillada de fin de semana", "cantidad": 2},
    {"comprador": "María", "evento": "Evento VIP de asado", "cantidad": 1}
]

# Datos de ejemplo para eventos
eventos_ejemplo = [
    {"nombre": "Parrillada de fin de semana", "fecha": "2024-03-20", "cantidad_disponible": 50, "precio": 20.0},
    {"nombre": "Evento VIP de asado", "fecha": "2024-04-15", "cantidad_disponible": 20, "precio": 50.0}
]

# Escribir datos de ejemplo en archivo ventas.json
ruta_ventas_json = os.path.join(directorio_actual, "..", "data", "ventas.json")
with open(ruta_ventas_json, "w") as file:
    json.dump(ventas_ejemplo, file, indent=4)

# Escribir datos de ejemplo en archivo eventos.json
ruta_eventos_json = os.path.join(directorio_actual, "..", "data", "eventos.json")
with open(ruta_eventos_json, "w") as file:
    json.dump(eventos_ejemplo, file, indent=4)

print("Datos de ejemplo escritos en los archivos ventas.json y eventos.json.")
