from time import sleep

class espadaVieja():
    def __init__(self):
        self.nombre = 'espada vieja'
        self.ataqueNormal = 250
        self.especial = 35
        self.energia = 100
        self.max_energia = self.energia

    def ejecucionAtaque(self,enemy,player):
        sleep(0.5)
        print("ahora atacaras")
        sleep(0.5)
        print(f'la vida del enemigo era:{enemy.vida}')
        sleep(0.5)
        enemy.vida -= self.ataqueNormal
        print(f"la vida del enemigo es: {enemy.vida}")
        sleep(0.5)
        return ""

    def ejeucionEspecial(self,enemy,player):
        print(f"este ataque es tan poderoso que te consume energia")
        sleep(1)
        print('pero en daño lo recompensa')
        requesitos = 30
        sleep(0.9)
        if self.energia >= requesitos:
            print("aqui tu ultimate ")
            sleep(1)
            print(f"la vida del {enemy.nombre} era de: {enemy.vida}")
            sleep(2)
            print(f"y tu energia era {self.energia}")
            sleep(2)
            enemy.vida -= self.especial
            self.energia = self.energia - requesitos
            print(f"ahora la energia es de {self.energia}")
            sleep(2)
            print(f"ahora el {enemy.nombre} tiene {enemy.vida} de vida")
            sleep(2)
        else:
            print("no puedes hacer el ataque especial te quedaste sin energia")
            sleep(2)
        return ""

    def restablecer_energia(self):
        sleep(0.5)
        print(f'tu enegia era de: {self.energia}')
        self.energia = self.max_energia
        sleep(0.5)
        return print(f"ahora tu enegia es: {self.energia}")

class espadaMetalica(espadaVieja):
    def __init__(self):
        self.nombre = "la espada metalica"
        self.ataqueNormal = 30
        self.especial = 40
        self.energia = 100

    def PocionFuria(self, mejora_ataques, mejora_energia):
        sleep(1)
        print("has activado el modo furia ")
        sleep(2)
        print(f"tu ataque normal era de {self.ataqueNormal}")
        self.ataqueNormal += mejora_ataques
        sleep(2)
        print(f"ahora el ataque normal es de {self.ataqueNormal}")
        sleep(2)
        print(f"tu especial hacia {self.especial}")
        self.especial += mejora_ataques
        sleep(1.5)
        print(f'tu especial ahora es de {self.especial}')
        sleep(2)
        print(f'tu energia hacido mejorara un +{mejora_energia}%')
        porcentaje = self.energia * mejora_energia / 100
        self.energia += porcentaje
        self.energia = int(self.energia)
        sleep(1)
        print(f"ahora tu energia es {self.energia}")
        return ""

    def ejeucionEspecial(self,enemy,player):
        requesitos = 30
        sleep(0.9)
        if self.energia >= requesitos:
            print("activaste el especial")
            sleep(1)
            print(f"la vida del {enemy.nombre} era de: {enemy.vida}")
            sleep(2)
            print(f"y tu energia era {self.energia}")
            sleep(2)
            enemy.vida -= self.especial
            self.energia = self.energia - requesitos
            print(f"ahora la energia es de {self.energia}")
            sleep(2)
            print(f"ahora el {enemy.nombre} tiene {enemy.vida} de vida")
            sleep(2)
        else:
            sleep(2)
            print("no puedes hacer el ataque especial te quedaste sin energia")
            sleep(1.3)
        return ""
