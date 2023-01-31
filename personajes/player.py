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
        print("tu: subi de nivel")
        sleep(1)
        print("tu: mi vida se multiplicara por 0.4")
        sleep(1)
        print(f"tu: mi vida era de {self.vida}")
        porcentaje = self.vida * 0.4
        self.vida = self.vida + porcentaje
        self.vida = int(self.vida)
        sleep(1)
        print(f"tu: ahora mi vida se le sumara {porcentaje} y ahora mi vida es: {self.vida}")
        self.max_vida = self.vida
        self.min_vida = self.max_vida - self.pocion
        sleep(1)
        return ""

    def subir_nivel(self):
        requerimientos = 100
        while self.exp >= requerimientos:
            print("tu: reuni la suficiente experiencia para subir de nivel")
            sleep(1)
            decicion = input("?: quiero subir de nivel Y/N")
            sleep(1)
            global nivel
            global exp
            decicion = decicion.upper()
            if decicion == 'Y':
                self.nivel += 1
                self.exp -= 100
                print(f"tu: ahora mi nivel es: {self.nivel}")
                sleep(1)
                eleccion = input("?: quiero recibir mi recompensa Y/N")
                eleccion = eleccion.upper()
                if eleccion == 'Y':
                    self.recompensas()
                    continue;
                else:
                    print('tu: no gracias no soy codicioso')
            elif decicion == 'N':
                sleep(0.5)
                print('ok')
                break;
            else:
                print("tu: que puse? ")
        return ""

    def curacion(self):
        if self.vida > self.max_vida:
            sleep(2)
            print("tu: me he pasado del limite de vida me pondran al original")
            sleep(2)
        
        elif self.vida == self.max_vida:
            sleep(2)
            print("tu: tengo mi vida llena para que quiero mas curacion? ")
            sleep(2)
            print(f"tu: mi vida era: {self.vida}")
            sleep(1)
            self.vida = self.max_vida
            print(f'tu: ahora mi vida es: {self.vida}')
            sleep(1)
        elif self.vida <= self.min_vida:
            print(f"tu: mi vida era de: {self.vida}")
            sleep(1.5)
            self.vida = self.vida + self.pocion
            print(f"tu: ahora mi vida es: {self.vida}")
            sleep(2)
        else:
            print("tu: no cumplo con los requesitos para curarme")
        return ""
        
    def restablecer_vida(self):
        sleep(2)
        print(f'tu: mi vida era de: {self.vida}')
        sleep(2)
        if self.vida != self.max_vida:
            self.vida = self.max_vida
        return print(f"tu: ahora mi vida es: {self.vida} :)")
        

class personajev2():
    pass