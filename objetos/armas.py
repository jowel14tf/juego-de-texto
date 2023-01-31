from time import sleep

class espadaVieja():
    def __init__(self):
        self.nombre = 'espada vieja'
        self.ataqueNormal = 25
        self.especial = 35
        self.energia = 100
        self.max_energia = self.energia

    def ejecucionAtaque(self,enemy,player):
        sleep(0.5)
        print("ahora atacaras")
        sleep(0.5)
        print(f'tu: tu vida era:{enemy.vida}')
        sleep(0.5)
        enemy.vida -= self.ataqueNormal
        print(f"tu: ahora es: {enemy.vida}")
        sleep(0.5)
        return ""

    def ejeucionEspecial(self,enemy,player):
        print(f"tu: con este ataque te enseñare lo que es bueno")
        requesitos = 30
        sleep(0.9)
        if self.energia >= requesitos:
            print('tu: VALISTE')
            sleep(1)
            print(f"tu: tu vida era: {enemy.vida}")
            sleep(2)
            print(f"tu: mi energia es: {self.energia}")
            sleep(2)
            enemy.vida -= self.especial
            self.energia = self.energia - requesitos
            print(f"mi#rd@ ahora mi energia es:{self.energia}")
            sleep(2)
            print(f"tu: ahora tienes {enemy.vida} de vida")
            sleep(2)
        else:
            print("tu: mi#rd@ me quede sin energia")
            sleep(2)
        return ""

    def restablecer_energia(self):
        sleep(0.5)
        print(f'tu: mi enegia era de: {self.energia}')
        self.energia = self.max_energia
        sleep(0.5)
        return print(f"tu: ahora mi enegia es: {self.energia}")

class espadaMetalica(espadaVieja):
    def __init__(self):
        self.nombre = "la espada metalica"
        self.ataqueNormal = 30
        self.especial = 40
        self.energia = 100
        self.max_energia = self.energia

    def PocionFuria(self, mejora_ataques, mejora_energia):
        sleep(1)
        print("tu: active el modo furia ")
        sleep(1)
        print("ve buscando donde mudarte")
        sleep(2)
        print(f"tu: mi ataque normal era: {self.ataqueNormal}")
        self.ataqueNormal += mejora_ataques
        sleep(2)
        print(f"tu: ahora mi ataque normal es: {self.ataqueNormal}")
        sleep(2)
        print(f"tu: mi especial hacia {self.especial}")
        self.especial += mejora_ataques
        sleep(1.5)
        print(f'tu: ahora mi especial ahora es {self.especial}')
        sleep(2)
        print(f'tu: mi energia hacido mejorara un +{mejora_energia}%')
        porcentaje = self.energia * mejora_energia / 100
        self.energia += porcentaje
        self.energia = int(self.energia)
        sleep(1)
        print(f"tu: ahora mi energia es: {self.energia}")
        return ""

    def ejeucionEspecial(self,enemy,player):
        requesitos = 30
        sleep(0.9)
        if self.energia >= requesitos:
            print("tu: active el especial")
            sleep(1)
            print(f"tu: tu vida era: {enemy.vida}")
            sleep(2)
            print(f"tu: mi energia era: {self.energia}")
            sleep(2)
            enemy.vida -= self.especial
            self.energia = self.energia - requesitos
            print(f"tu: ahora mi energia es: {self.energia}")
            sleep(2)
            print(f"tu: ahora tu vida es: {enemy.vida}")
            sleep(2)
        else:
            sleep(2)
            print("tu: no puedo hacer el especial me quede sin energia")
            sleep(1.3)
        return ""
