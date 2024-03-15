# comprador.py

from persona import Persona

class Comprador(Persona):
    def __init__(self, nombre, email, saldo):
        super().__init__(nombre, email)
        self.saldo = saldo

    def actualizar_saldo(self, cantidad):
        self.saldo += cantidad



