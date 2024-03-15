# interfaz_grafica.py

# Importa la biblioteca gráfica que estés utilizando
# Por ejemplo, si estás usando Tkinter, importa así:
# import tkinter as tk

class InterfazGrafica:
    def __init__(self, gestor_ventas):
        self.gestor_ventas = gestor_ventas
        # Inicializa la ventana y los widgets de la interfaz gráfica aquí

    def mostrar_interfaz(self):
        # Define la disposición de los widgets y configura los eventos de la interfaz gráfica aquí
        pass

# Ejemplo de uso:
if __name__ == "__main__":
    from gestor_ventas import GestorVentas
    
    # Crear una instancia de GestorVentas
    gestor_ventas = GestorVentas()
    
    # Crear una instancia de la interfaz gráfica
    interfaz_grafica = InterfazGrafica(gestor_ventas)
    
    # Mostrar la interfaz gráfica
    interfaz_grafica.mostrar_interfaz()
