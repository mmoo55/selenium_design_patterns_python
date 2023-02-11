
class ClienteEntity:

    def __init__(self, id = 0, nombres = "", apellidos = ""):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombres(self):
        return self.nombres

    def set_nombres(self, nombres):
        self.nombres = nombres

    def get_apellidos(self):
        return self.apellidos

    def set_apellidos(self, apellidos):
        self.apellidos = apellidos