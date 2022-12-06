

class personaje():
    def __init__(self,nombre,vida,arma):
        self.nombre = nombre
        self.vida = vida
        self.arma = arma
        self.nivel = 1

    def subir_nivel(self,snivel):
        self.nivel = snivel
        return self.nivel

    def mostrar_vida(self):
        return f"tu vida es {self.vida}"
    
    def restablecer_vida(self,my):
        if my.vida != 100:
            my.vida = 100
        return f"tu vida ahora es: {my.vida} "