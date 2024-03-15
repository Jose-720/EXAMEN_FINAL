# organizador.py

from persona import Persona

class Organizador(Persona):
    def __init__(self, nombre, email, organizacion):
        super().__init__(nombre, email)
        self.organizacion = organizacion


