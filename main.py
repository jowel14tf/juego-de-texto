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

print(f"lider: {nombre} tu primera arma sera la {espada.nombre}")
sleep(2)
print("lider: es hora de enfrentarte a tu primer enemigo")
sleep(2)

print("lider: es un soldado tracionero, este tiene cierta informacion")
sleep(2)

print('lider: que nos puedes perjudicar asi que...')
sleep(2)

print('lider: hay que mandarlo a dormir en silencio sin que nadie sepa')
sleep(2)
print("tu: ??? ", "(dudas en silencio)")
sleep(2)
print("tu: ok lider hare mi mision")
sleep(1.9)
print("despues de tardar 1 hora lo encuentra asi que la batalla comienza")
sleep(1.6)

def battallaEspadaVieja(jugador,enemigo):
    global ganador
    global ataco
    global SeCuro
    ataco = False
    ganador = False
    SeCuro = False
    while jugador.vida >= 0 or enemigo.vida >= 0:
        
        if jugador.vida <= 0:
            print("tu: perdi...")
            eleccion = input(f"?: lo intento de nuevo {jugador.nombre} y/n")

            if eleccion == "y" or eleccion == " y":
                jugador.restablecer_vida()
                enemigo.restablecer_vida()
                espada.restablecer_energia()
                print(f"tu: tengo mi vida en: {jugador.vida}")
                print(f"enemigo: tengo mi vida en {enemigo.vida}")

            elif eleccion == "n" or eleccion == " n":
                print("tu: me rindo")
                break;
        
        print("tu: mi turno")

        eleccion = int(input(f"""
1) atacarlo                                           tu: mi vida es: {jugador.vida}
2) curarse ---> {jugador.pocion}                                    enemigo: mi vida es: {enemigo.vida}       
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
                print("cual es ese ataque")
                continue
        
        elif eleccion == 2:
            sleep(1)
            jugador.curacion()
            SeCuro = True

        else:
            print("tu: no hay opcion que tenga ese ataque")
            continue

        if enemigo.vida <= 0:
            print(f"tu: bien le gane al {enemigo.nombre}")
            jugador.restablecer_vida()
            espada.restablecer_energia()
            enemigo.vida = 110
            ganador = True
            if ganador == True:
                jugador.exp = 100
                jugador.subir_nivel()
                sleep(1)
                eleccion = input("?: pero te voy a hacer una pregunta en verdad crees que lo derrotaste y/y")
                sleep(0.5)
                print('.')
                sleep(0.5)
                print('.')
                sleep(0.5)
                print('.')
                sleep(0.5)
                if eleccion == "y" or eleccion == " y":
                    print(f"?: {jugador.nombre} pues...")
                    sleep(1.5)
                    print("?: quien se esta levantando detras tuyo ???")
                    sleep(2.2)
                    print("tu: fuera")
                    sleep(0.5)
                    print("tu: no te tengo miedo espiritu del mal fuera demonio")
                    sleep(3)
                break;
        
        if ataco == True or SeCuro == True:
            print("enemigo: ahora te atacare")
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
        print("tu: bien he conseguido una arma buena ")
        sleep(2)
        print(f'tu: consegui la {espadav2.nombre}')
        sleep(2)
        print("tu: esta arma tiene tiene mas daño y tiene un habilidad nueva \nllamada modo furia")
        sleep(1)
        curarse = 0

        eleccion = input("tu: quiero activar el modo furia y/n")
        if eleccion == 'y' or eleccion == ' y':
            espadav2.PocionFuria(10, 30)
        else:
            print("tu: no tengo activado el modo furia")
        
        ataco = False
        ganador = False
        SeCuro = False
        
        while jugador.vida > 0 or enemigo.vida > 0:

            if jugador.vida <= 0:
                print("tu: perdi...")
                eleccion = input(f"tu: quiero volver a intentarlo de nuevo y/n")

                if eleccion == "y" or eleccion == " y":
                    jugador.restablecer_vida()
                    enemigo.restablecer_vida()
                    espadav2.restablecer_energia()
                    print(f"tu: mi vida es: {jugador.vida}")
                    print(f"enemigo: mi vida es: {enemigo.vida}")

                elif eleccion == "n" or eleccion == " n":
                    print("tu: me rindo")
                    break;
            
            print("tu: es mi turno")

            eleccion = int(input(f"""
1) atacarlo                                             tu: mi vida es: {jugador.vida}
2) curarse ---> {jugador.pocion}                                    enemigo: mi vida es: {enemigo.vida}       
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
                    print("?: que ataque es ese?")
                    continue
            
            elif eleccion == 2:
                sleep(1)
                print("tu: me voy a curar")
                sleep(1)
                jugador.curacion()
                SeCuro = True

            else:
                print("tu: introduje nada XD")
                continue

            if enemigo.vida <= 0:
                print("tu: derrote al soldado otra vez")
                sleep(1)
                jugador.exp = 150
                jugador.restablecer_vida()
                jugador.subir_nivel()
                espadav2.restablecer_energia()
                sleep(1)
                print("tu: ahora si me asegurare de matarte...\nla vida del enemigo es: -174")
                sleep(1)
                print("enemigo: yo no tenia ninguna informacion ellos te minteron")
                sleep(2)
                print("enemigo: iva a filtrar todas sus verdades ellos son los malos")
                sleep(2)
                print("enemigo: hazme un favor no confies en nadie")
                sleep(2)
                print("tu: sera verdad lo que me dijo ?")
                sleep(2)
                print("tu: despues de un rato me queda pensando y llege a la conclusion de")
                sleep(3)
                print("fin del capitulo 1")
                break;

            if ataco == True or SeCuro == True:
                print("enemigo: ahora me toca a mi")
                num1, num2 = 0, 2
                Resultado = random.randint(num1, num2)
                
                if Resultado == 0:
                    print("enemigo: elegi hacer un ataque normal")
                    enemigo.RestarAtaquesNormales(jugador, enemigo)
                    ataco = False
                    SeCuro = False
                    del(num1, num2)
                
                elif Resultado == 1:
                    print('enemigo: eligio hacer mi ataque ESPECIAL')
                    enemigo.ejeucionEspecial(enemigo, jugador)
                    ataco = False
                    SeCuro = False
                    del(num1, num2)

                elif Resultado == 2:
                    curarse += 1
                    if curarse >= 3:
                        print("enemigo: intento curarse pero no puedo \n se me acabo las pociones :(")
                        sleep(2.5)
                        print("enemigo: tengo que dejar las drog, digo las pociones :)")
                        continue
                    else:
                        print("enemigo: eligi curarme")
                        enemigo.curacion()
                        ataco = False
                        SeCuro = False
                        del(num1, num2)

    batallaEspadaMetalica(jugador, soldadov2)
else:
    print("?: si tu no subes de nivel no puedes seguir con mi historia :(")
