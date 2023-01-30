from time import sleep
from personajes.player import personaje
from objetos.armas import espadaVieja
from enemigos.soldado import soldadoF1

print('capitulo 1 el comienzo de un heroe y sus enseñansas')
sleep(1)

nombre = input("""cual es tu nombre aventurero:
""")

espada = espadaVieja()

jugador = personaje(nombre, espada)

soldado = soldadoF1()

print(f"ok {nombre} tu primera arma sera la {espada.nombre}")
"""
print("es hora de enfrentarte a tu primer enemigo")
sleep(2)

print("es un soldado renegado y tiene cierta informacion")
sleep(2)

print('que nos puedes perjudicar asi que...')
sleep(2)

print('hay que mandarlo a dormir')
sleep(2)
print("despues de tardar 1 hora lo encuentra asi que la batalla comienza")
"""
def battallaEspadaVieja(jugador,enemigo):
    global ganador
    global ataco
    global SeCuro
    ataco = False
    ganador = False
    SeCuro = False
    while jugador.vida >= 0 or enemigo.vida >= 0:
        
        if jugador.vida <= 0:
            print("perdiste...")
            eleccion = input(f"quieres volver a intentarlo {jugador.nombre} otra vez y/n")

            if eleccion == "y" or eleccion == " y":
                jugador.restablecer_vida()
                enemigo.restablecer_vida()
                espada.restablecer_energia()
                print(f"{jugador.nombre} tiene su vida en {jugador.vida}")
                print(f"{enemigo.nombre} tiene su vida en {enemigo.vida}")

            elif eleccion == "n" or eleccion == " n":
                print("ok bye")
                break;
        
        print("es tu turno")

        eleccion = int(input(f"""
1) atacar                                               la vida del jugador es: {jugador.vida}
2) curarse ---> {jugador.pocion}                                      la vida del enemigo es: {enemigo.vida}       
"""))
        
        if eleccion == 1:
            ataques = int(input(f"""
1) ataque normal ---> {espada.ataqueNormal}
2)   especial ------> {espada.especial}
"""))
            if ataques == 1:
                espada.ejecucionAtaque(enemy=enemigo, player=jugador)
                ataco = True
            elif ataques == 2:
                espada.ejeucionEspecial(enemigo, jugador)
                ataco = True
            else:
                print("valor erroneo")
                continue
        
        elif eleccion == 2:
            sleep(1)
            print("ok has elegido curarte")
            sleep(1)
            jugador.curacion()
            SeCuro = True

        else:
            print("has introducido un valor erroneo por favor intentar de nuevo")
            continue

        if enemigo.vida <= 0:
            print(f"bien ganaste {jugador.nombre}")
            jugador.restablecer_vida()
            espada.restablecer_energia()
            enemigo.vida = 110
            ganador = True
            if ganador == True:
                print(f"bien le ganaste al {enemigo.nombre}")
                sleep(1)
                print("subiste de nivel ")
                jugador.exp = 100
                jugador.subir_nivel()
                sleep(1)
                eleccion = input("pero te voy a hacer una pregunta en verdad crees que lo derrotaste y/y")
                sleep(0.5)
                print('.')
                sleep(0.5)
                print('.')
                sleep(0.5)
                print('.')
                sleep(0.5)
                if eleccion == "y" or eleccion == " y":
                    print(f"{jugador.nombre} pues...")
                    sleep(1.5)
                    print("quien se esta levantando detras tuyo ???")
                    sleep(2.2)
                    print("ten buena suerte con mi ataque ESPECIAL ")
                break;
        
        if ataco == True or SeCuro == True:
            print("ahora el soldado te atacara")
            enemigo.RestarAtaquesNormales(player=jugador, enemigo=soldado)
            ataco = False
            SeCuro = False
        

battallaEspadaVieja(jugador, soldado)

from objetos.armas import espadaMetalica
from enemigos.soldado import soldadoF2
import random

espadav2 = espadaMetalica()
soldadov2 = soldadoF2()

if jugador.nivel == 1:
    def batallaEspadaMetalica(jugador, enemigo):
        print("bien has conseguido una arma decente ")
        sleep(2)
        print(f'has conseguido {espadav2.nombre}')
        sleep(2)
        print("esta arma tiene tiene mas daño y tiene un habilidad nueva \nllamada modo furia")
        sleep(1)

        eleccion = input("quieres activar el modo furia de la espada y/n")
        if eleccion == 'y' or eleccion == ' y':
            espadav2.PocionFuria(10, 30)
        else:
            print("no tienes activado el modo furia")
        
        ataco = False
        ganador = False
        SeCuro = False
        
        while jugador.vida > 0 or enemigo.vida > 0:

            if jugador.vida <= 0:
                print("perdiste...")
                eleccion = input(f"quieres volver a intentarlo {jugador.nombre} otra vez y/n")

                if eleccion == "y" or eleccion == " y":
                    jugador.restablecer_vida()
                    enemigo.restablecer_vida()
                    espadav2.restablecer_energia()
                    print(f"{jugador.nombre} tiene su vida en {jugador.vida}")
                    print(f"{enemigo.nombre} tiene su vida en {enemigo.vida}")

                elif eleccion == "n" or eleccion == " n":
                    print("ok bye")
                    break;
            
            print("es tu turno")

            eleccion = int(input(f"""
1) atacar                                               la vida del jugador es: {jugador.vida}
2) curarse ---> {jugador.pocion}                                      la vida del enemigo es: {enemigo.vida}       
"""))
            if eleccion == 1:
                ataques = int(input(f"""
1) ataque normal ---> {espadav2.ataqueNormal}
2)   especial ------> {espadav2.especial}
"""))
                if ataques == 1:
                    espadav2.ejecucionAtaque(enemy=enemigo, player=jugador)
                    ataco = True

                elif ataques == 2:
                    espadav2.ejeucionEspecial(enemigo, jugador)
                    ataco = True

                else:
                    print("valor erroneo")
                    continue
            
            elif eleccion == 2:
                sleep(1)
                print("ok has elegido curarte")
                sleep(1)
                jugador.curacion()
                SeCuro = True

            else:
                print("has introducido un valor erroneo por favor intentar de nuevo")
                continue

            if enemigo.vida <= 0:
                print('fui derrotado')
                break;

            if ataco == True or SeCuro == True:
                print("ahora le toca al soldado atacar")
                num1, num2 = 0, 2
                Resultado = random.randint(num1, num2)
                
                if Resultado == 0:
                    print("el soldado ha elegido hacer un ataque normal")
                    enemigo.RestarAtaquesNormales(jugador, enemigo)
                    ataco = False
                    SeCuro = False
                    del(num1, num2)
                
                elif Resultado == 1:
                    print('el soldado eligio su ataque especial')
                    enemigo.ejeucionEspecial(enemigo, jugador)
                    ataco = False
                    SeCuro = False
                    del(num1, num2)

                elif Resultado == 2:
                    print("el soldado eligio curarse")
                    enemigo.curacion()
                    ataco = False
                    SeCuro = False
                    del(num1, num2)

    batallaEspadaMetalica(jugador, soldadov2)
else:
    print("si no subes de nivel no puedes seguir con la historia :(")