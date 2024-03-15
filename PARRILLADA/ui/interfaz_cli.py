# interfaz_cli.py

class InterfazCLI:
    def __init__(self, gestor_ventas):
        self.gestor_ventas = gestor_ventas

    def mostrar_menu_principal(self):
        while True:
            print("----- Menú Principal -----")
            print("1. Realizar venta")
            print("2. Generar reporte de ventas")
            print("3. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.realizar_venta()
            elif opcion == "2":
                self.generar_reporte_ventas()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def realizar_venta(self):
        # Aquí puedes implementar la lógica para realizar una venta
        pass

    def generar_reporte_ventas(self):
        reporte = self.gestor_ventas.generar_reporte_ventas()
        print("----- Reporte de Ventas -----")
        for evento, cantidad in reporte.items():
            print(f"{evento}: {cantidad} tickets vendidos")

# Ejemplo de uso:
if __name__ == "__main__":
    from gestor_ventas import GestorVentas
    
    # Crear una instancia de GestorVentas
    gestor_ventas = GestorVentas()
    
    # Crear una instancia de la interfaz CLI
    interfaz_cli = InterfazCLI(gestor_ventas)
    
    # Mostrar el menú principal
    interfaz_cli.mostrar_menu_principal()
