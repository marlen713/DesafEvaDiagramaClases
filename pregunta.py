class Pregunta:
    def __init__(self, enunciado, ayuda=None, requerida=False):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.lista_de_alternativas = []
    
    def mostrar_pregunta(self):
        pass