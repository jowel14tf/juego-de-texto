class enemigo():
    
    def __init__(self,nombre,vida,ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque 

    def atacar(self):
        return True
    
    def restablecer_vida(self,my):
        if my.vida != 100:
            my.vida = 100
        return f"la vida del enemigo ahora es {my.vida}"