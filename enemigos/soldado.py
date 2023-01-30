from time import sleep

class soldadoF1():
    def __init__(self):
        self.nombre = 'soldado'
        self.vida = 110
        self.ataqueNormal = 25

    def RestarAtaquesNormales(self, player, enemigo):
        sleep(1)
        print(f'tenias {player.vida} de vida ')
        accion = player.vida = player.vida - enemigo.ataqueNormal
        sleep(1.6)
        return print(f"y ahora tienes {accion} de vida")


    def restablecer_vida(self):
        sleep(1.5)
        print(f'la vida del enemigo era de: {self.vida}')
        if self.vida != 100:
            self.vida = 100
            sleep(1.2)
        return print(f"ahora la vida es de:{self.vida}")

class soldadoF2(soldadoF1):
    def __init__(self):
        self.nombre = "soldado vengativo"
        self.vida = 140
        self.ataqueNormal = 30
        self.especial = 35
        self.pocion = 20
        self.max_vida = self.vida
        self.min_vida = self.max_vida - self.pocion

    def ejeucionEspecial(self,enemy,player):
        print("este es el ataque mas poderoso del soldado su ESPECIAL")
        sleep(1)
        print("aqui va su ataque")
        sleep(1)
        self.vida
        print(f"la vida de {player.nombre} era de: {player.vida}")
        sleep(1.3)
        player.vida -= self.especial
        print(f"ahora {player.nombre} tiene {player.vida} de vida")
        sleep(1.4)    
        return ""

    def curacion(self):
        sleep(1.3)
        print("el enemigo ha elegido curarse ")
        sleep(1.2)
        print(f"la vida del enemigo era {self.vida}")
        self.vida += self.pocion
        sleep(1)
        print(f"ahora la vida del enemigo es {self.vida}")
        sleep(2)
        return ""

    def restablecer_vida(self):
        sleep(1)
        print(f'la vida del enemigo era de: {self.vida}')
        if self.vida != self.max_vida:
            self.vida = self.max_vida
            sleep(1.3)
            print(f"ahora la vida es de:{self.vida}")
        return ''

### RECONSTRUIR LA CLASE Y QUE NO SEA OGRO QUE SEA MEJOR 
class Mago():
    pass

