class Encuesta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_de_preguntas = []
        self.lista_de_listados_de_respuestas = []

    def mostrar_encuesta(self):
         pass

    def agregar_listado_respuestas(self):
        pass

class EncuestaLimitadaEdad:
    def __init__(self, edad_minima, edad_maxima):
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

class EncuestaLimitadaRegion:
    def __init__(self, lista_de_regiones):
        self.lista_de_regiones = lista_de_regiones

