from time import sleep

class personaje():
    def __init__(self,nombre,arma):
        
        self.nombre = nombre
        self.vida = 120
        self.pocion = 30
        self.max_vida = self.vida
        self.min_vida = self.max_vida - self.pocion
        self.arma = arma
        self.exp = 100
        self.nivel = 0

    def recompensas(self):
        print("ya que subiste de nivel")
        sleep(1)
        print("tu vida se multiplicara por 0.4")
        sleep(1)
        print(f"tu vida era de {self.vida}")
        porcentaje = self.vida * 0.4
        self.vida = self.vida + porcentaje
        self.vida = int(self.vida)
        sleep(1)
        print(f"ahora tu vida se le sumara {porcentaje} y ahora tu vida es: {self.vida}")
        self.max_vida = self.vida
        self.min_vida = self.max_vida - self.pocion
        sleep(1)
        return ""

    def subir_nivel(self):
        requerimientos = 100
        while self.exp >= requerimientos:
            print("reuniste la suficiente experiencia para subir de nivel")
            sleep(1)
            decicion = input("quieres subir de nivel Y/N")
            sleep(1)
            global nivel
            global exp
            decicion = decicion.upper()
            if decicion == 'Y':
                self.nivel += 1
                self.exp -= 100
                print(f"ahora eres de nivel {self.nivel}")
                sleep(1)
                eleccion = input("quieres recibir tu recompensa Y/N")
                eleccion = eleccion.upper()
                if eleccion == 'Y':
                    self.recompensas()
                    continue;
                else:
                    print('ok')
            elif decicion == 'N':
                sleep(0.5)
                print('ok')
                break;
            else:
                print("valor incorrecto por favor verifique bien")
        return ""

    def curacion(self):
        if self.vida > self.max_vida:
            sleep(2)
            print("te has pasado del limite de vida establecido te retauraremos a tu vida original")
            sleep(2)
        
        elif self.vida == self.max_vida:
            sleep(2)
            print("tienes tu vida llena no hace falta curarse")
            sleep(2)
            print(f"tu vida era de {self.vida}")
            sleep(1)
            self.vida = self.max_vida
            print(f'ahora tu vida es de {self.vida}')
            sleep(1)
        elif self.vida <= self.min_vida:
            print(f"tu vida era de: {self.vida}")
            sleep(1.5)
            self.vida = self.vida + self.pocion
            print(f"ahora tu vida es: {self.vida}")
            sleep(2)
        return ""
        
    def restablecer_vida(self):
        sleep(2)
        print(f'tu vida era de: {self.vida}')
        sleep(2)
        if self.vida != self.max_vida:
            self.vida = self.max_vida
        return print(f"ahora tu vida es: {self.vida}")
        

class personajev2():
    pass