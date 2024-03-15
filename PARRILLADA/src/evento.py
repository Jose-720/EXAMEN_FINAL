# evento.py

class Evento:
    def __init__(self, nombre, fecha, cantidad_disponible, precio):
        self.nombre = nombre
        self.fecha = fecha
        self.cantidad_disponible = cantidad_disponible
        self.precio = precio

    def actualizar_disponibilidad(self, cantidad):
        self.cantidad_disponible += cantidad


