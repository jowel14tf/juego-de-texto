
class ogroo():

    nombre = "Ogro"
    vida = 115
    ataque = 30

    def garrotazo(self):
        return True
    
    def InformacionOgroo(self):
        caracteristicas = f"""
su nombre es: {self.nombre}
tiene una vida de: {self.vida}
tiene un ataque de: {self.ataque}
        """
        return caracteristicas
    
    
    def restablecer_vida(self,my):
        if my.vida != 100:
            my.vida = 100
        return f"la vida del enemigo ahora es {my.vida}"