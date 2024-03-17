

class Usuario:
    def __init__(self, correo, edad, region):
        self.correo = correo
        self.edad = edad
        self.region = region
    
    def contestar_encuesta(self):
        pass

class ListadoRespuestas:
    def __init__(self, usuario, lista_de_respuestas):
        self.usuario = usuario
        self.lista_de_respuestas = lista_de_respuestas