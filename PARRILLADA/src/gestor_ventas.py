# gestor_ventas.py

import json

class GestorVentas:
    def __init__(self):
        self.ventas = []
        self.eventos = []

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def cargar_ventas_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as file:
                ventas = json.load(file)
                self.ventas.extend(ventas)
                print("Ventas cargadas correctamente desde el archivo:", nombre_archivo)
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {nombre_archivo}.")

    def cargar_eventos_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as file:
                eventos = json.load(file)
                self.eventos.extend(eventos)
                print("Eventos cargados correctamente desde el archivo:", nombre_archivo)
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
        except json.JSONDecodeError:
            print(f"Error al decodificar el archivo {nombre_archivo}.")

    def guardar_ventas_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as file:
            json.dump(self.ventas, file, indent=4)

    def generar_reporte_ventas(self):
        reporte = {}
        for venta in self.ventas:
            evento_nombre = venta.evento.nombre
            if evento_nombre in reporte:
                reporte[evento_nombre] += venta.cantidad
            else:
                reporte[evento_nombre] = venta.cantidad
        return reporte

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una instancia de GestorVentas
    gestor_ventas = GestorVentas()
    # Cargar ventas desde un archivo
    gestor_ventas.cargar_ventas_desde_archivo("data/ventas.json")
    # Cargar eventos desde un archivo
    gestor_ventas.cargar_eventos_desde_archivo("data/eventos.json")
