import time
#importando objetos
from objetos.espadas import *
from personajes.personaje import *
from enemigos.soldado import *
from habilidad.habilidades import *
from enemigos.ogro import ogroo
from objetos.arco import arcoo
#advertencia
print("nota: ignora los NONE que aparecen en la terminal")
time.sleep(1)
#comienzo 
print('capitulo 1 el comienzo de un heroe')
time.sleep(1)
nombre = input("cual es tu nombre")
nivel = 1
exp = 0
#decide entre si o no
time.sleep(1)
eleccion = input(f"bueno... {nombre} quieres usar la espada ? si o no")
time.sleep(1)
if eleccion == " si" or eleccion == 'si':
    player = personaje(nombre, 100, sword())
    print("bien! pues aqui comienza tu aventura")
    time.sleep(0.5)
else:
    print("pues aqui acaba el juego ¯ \ _ (ツ) _ / ¯ ")




soldado = enemigo("soldado", 85, 25)

#el sistema para que se ejecute una batalla
def ganaste(verificador):
    gano = verificador
    return gano
def batalla_soldadov_1(jugador,enemigo):
    print("no puedes usar mas de 3 vez el especial o si no te tiraremos un error")
    time.sleep(0.5)
    print("iniciaras primero")
    time.sleep(0.5)
    contador = 0
    actualizador = False
    while jugador.vida > 0 and enemigo.vida > 0:

        if contador > 3:
            time.sleep(1)
            raise ValueError("te has pasado de intentos y tendras que iniciar de CERO")
            
        time.sleep(0.5)
        eleccion_batalla = input(f'que ataques haras ? remolino / ataque normal / especial')
            
        if eleccion_batalla == "remolino" or eleccion_batalla == ' remolino':
            if sword.remolino(True) == True: 
                enemigo.vida = enemigo.vida - sword.remolino_o
                time.sleep(0.5)
                print(f"la vida del enemigo ahora es: {enemigo.vida}")
                actualizador = True

        elif eleccion_batalla == 'ataque normal' or eleccion_batalla == ' ataque normal':
            if sword.ataque_normal(True) == True:
                enemigo.vida = enemigo.vida - sword.ataque_normal_o
                time.sleep(0.5)
                print(f'la vida del enemigo ahora es: {enemigo.vida}')
                actualizador = True

        elif eleccion_batalla == 'especial' or eleccion_batalla == ' especial':
            contador = contador + 1
            if sword.especial(True) == True:
                enemigo.vida = enemigo.vida - sword.especial_o
                time.sleep(0.5)
                print(f'la vida del enemigo ahora es: {enemigo.vida}')
                actualizador = True
        else:
            print("no hay ningun ataque con ese nombre!")

        if actualizador == True:
            time.sleep(0.5)
            print(f"ahora le toca al {enemigo.nombre} atacar ")
            enemigo.atacar()
            if enemigo.atacar() == True:
                player.vida = player.vida - enemigo.ataque
                time.sleep(0.5)
                print(f"ahora tu vida es: {player.mostrar_vida()}")
                actualizador = False
        
        if enemigo.vida <= 0:
            time.sleep(0.5)
            print("Bien ganaste a tu primer enemigo!!! \n tu vida esta con una leve mejora")
            time.sleep(0.5)
            print("subiste de nivel a nivel de 2")
            player.restablecer_vida(player)
            ganaste(True)
            break;

        elif player.vida <= 0:
            time.sleep(0.5)
            print("Que mal perdiste... \n pero aun es muy temprano para rendirte!")
            time.sleep(1)
            print("intentemoslo otra vez!")
            player.restablecer_vida(player)
            enemigo.restablecer_vida(enemigo)
            ganaste(False)

eleccion = input(f'un {soldado.nombre} quiere atacar que vas a hacer?, luchar o huir')
time.sleep(0.9)
if eleccion == "luchar" or eleccion == ' luchar':
    batalla_soldadov_1(player, soldado)

elif eleccion == "huir" or eleccion == " huir":
    print("no seas cobarde... \n ENFRENTATE")
    batalla_soldadov_1(player, soldado)

else:
    print('no hay una opcion con ese nombre\n intentalo de nuevo')
    eleccion = input(f'un {soldado.nombre} quiere atacar que vas a hacer?, luchar o huir')
    eleccion = input(f'un {soldado.nombre} quiere atacar que vas a hacer?, luchar o huir')
    eleccion = input(f'un {soldado.nombre} quiere atacar que vas a hacer?, luchar o huir')


#mejoras

if  ganaste(True) == True:
    player.vida = 120
    print("tu recompensas son: el plus, la mejora de vida")
    time.sleep(1)
    print(f"ya que ganaste ahora tu vida vale {player.vida}")
    time.sleep(1)
    print("desbloqueaste una nueva habilidad llamada plus!!! \n esta se podra activar con un ataque ")
    time.sleep(1)
    print("por ejemplo remolino / plus")
    time.sleep(1)
    print("el plus lo que hace es que el ataque que pongas recibira 5 de dano extra ")
    time.sleep(1)

player.subir_nivel(2)
print(f"tu nivel ahora es: {player.nivel}")

habilidad = [
    ["tienes la habilidad plus"],
    ["tienes la habilidad omega"],
    ["tienes la habilidad ultra"],
    ["tienes la habilidad ultraplus"],
]


print("despues de vencer al soldado se te desbloquean algunos camino para recorer ")
time.sleep(1)
decicion = input("izquierda o derecha")
time.sleep(1)

def ganaste(verificador):
    gano = verificador
    return gano

def batalla_ogro(jugador,enemigo):
    print("no puedes usar mas de 3 vez el especial o si no te tiraremos un error")
    time.sleep(0.5)
    print("iniciaras primero")
    time.sleep(0.5)
    contador = 0
    actualizador = False
    while jugador.vida > 0 and enemigo.vida > 0:

        if contador > 3:
            time.sleep(1)
            raise ValueError("te has pasado de intentos y tendras que iniciar de CERO")
            
        time.sleep(0.5)
        eleccion_batalla = input(f"""
que ataque haras:

sin habilidad:        con habilidad:

remolino              remolino / plus  
ataque normal         ataque normal / plus 
especial              especial / plus

""")
            
        if eleccion_batalla == "remolino" or eleccion_batalla == ' remolino':
            if sword.remolino(True) == True: 
                enemigo.vida = enemigo.vida - sword.remolino_o
                time.sleep(0.5)
                print(f"la vida del enemigo ahora es: {enemigo.vida}")
                actualizador = True

        elif eleccion_batalla == 'ataque normal' or eleccion_batalla == ' ataque normal':
            if sword.ataque_normal(True) == True:
                enemigo.vida = enemigo.vida - sword.ataque_normal_o
                time.sleep(0.5)
                print(f'la vida del enemigo ahora es: {enemigo.vida}')
                actualizador = True

        elif eleccion_batalla == 'especial' or eleccion_batalla == ' especial':
            contador = contador + 1
            if sword.especial(True) == True:
                enemigo.vida = enemigo.vida - sword.especial_o
                time.sleep(0.5)
                print(f'la vida del enemigo ahora es: {enemigo.vida}')
                actualizador = True

        elif eleccion_batalla == " remolino / plus" or eleccion_batalla == "remolino / plus":
            if sword.remolino(True) == True:
                sword.remolino_o = sword.remolino_o + habilidades.plus
                enemigo.vida = enemigo.vida - sword.remolino_o
                time.sleep(0.5)
                print(f"la vida del enemigo ahora es: {enemigo.vida}")
                actualizador = True
                sword.remolino_o -= habilidades.plus
                

        elif eleccion_batalla == " ataque normal / plus" or eleccion_batalla == "ataque normal / plus":
            if sword.ataque_normal(True) == True:
                sword.ataque_normal_o = sword.ataque_normal_o + habilidades.plus
                enemigo.vida = enemigo.vida - sword.ataque_normal_o
                time.sleep(0.5)
                print(f"la vida del enemigo ahora es: {enemigo.vida}")
                actualizador = True
                sword.ataque_normal_o -= habilidades.plus

        elif eleccion_batalla == "especial / plus" or eleccion_batalla == " especial / plus":
            contador = contador + 1
            if sword.especial(True) == True:
                sword.especial_o = sword.especial_o + habilidades.plus
                enemigo.vida = enemigo.vida - sword.especial_o
                time.sleep(0.5)
                print(f"la vida del enemigo ahora es: {enemigo.vida}")
                actualizador = True
                sword.especial_o -= habilidades.plus

        else:
            print("no hay ningun ataque con ese nombre!")
            time.sleep(0.5)
        if actualizador == True:
            time.sleep(0.5)
            print(f"ahora le toca al {enemigo.nombre} atacar ")
            enemigo.garrotazo(self=ogroo)
            if enemigo.garrotazo(self=ogroo) == True:
                player.vida = player.vida - enemigo.ataque
                time.sleep(0.5)
                print(f"ahora tu vida es: {player.mostrar_vida()}")
                actualizador = False
        
        if enemigo.vida <= 0:
            time.sleep(0.5)
            print("Bien le ganaste al ogro!!! \n tu vida esta con una leve mejora")
            time.sleep(0.5)
            print("mejoraste de nivel a nivel 3")
            player.restablecer_vida(player)
            ganaste(True)
            break;

        elif player.vida <= 0:
            time.sleep(0.5)
            print("Que mal perdiste... \n pero aun es muy temprano para rendirte!")
            time.sleep(1)
            print("intentemoslo otra vez!")
            player.restablecer_vida(player)
            enemigo.restablecer_vida(enemigo)
            ganaste(False)



def ganaste(verificador):
    gano = verificador
    return gano
def batalla__ogro_arco(jugador,enemigo):
    print("no puedes usar mas de 3 veces el flechazo sangriento por que si no te tiraremos un error")

    print("iniciaras primero")
    actualizador = False
    while jugador.vida > 0 and enemigo.vida > 0:
        arcoo.flechas = 10
        eleccion = input("""
que tipo de flechazo vas a elegir:

sin habilidad                 con hablidad

flechazo                      flechazo / plus
flechazo preciso              flechazo preciso / plus
flechazo sangriento           flechazo sangriento / plus

""")

        if eleccion == "flechazo" or eleccion == " flechazo":
            arco.flechazo()
            actualizador = True
            if arco.flechazo() == True:
                enemigo.vida -= 20
                time.sleep(1)
                print(f"la vida del enemigo ahora es: {enemigo.vida}")

        elif eleccion == "flechazo preciso" or eleccion == " flechazo preciso":
            arco.flechazo_preciso()
            actualizador = True
            if arco.flechazo_preciso() == True:
                enemigo.vida -= 25
                time.sleep(1)
                print(f"la vida del enemigo ahora es: {enemigo.vida}")
                
        elif eleccion == "flechazo sangriento" or eleccion == " flechazo sangriento":
            arco.flechazo_sangriento()
            actualizador = True
            if arco.flechazo_sangriento() == True:
                enemigo.vida -= 40
                time.sleep(1)
                print(f"la vida del enemigo ahora es: {enemigo.vida}")
                
        elif eleccion == "flechazo / plus" or eleccion == " flechazo / plus":
            arco.flechazo()
            actualizador = True
            if arco.flechazo() == True:
                enemigo.vida -= 25
                time.sleep(1)
                print(f'la vida del enemigo ahora es: {enemigo.vida}')
                
        elif eleccion == "flechazo preciso / plus" or eleccion == " flechazo / plus":
            arco.flechazo_preciso()
            actualizador = True
            if arco.flechazo_preciso() == True:
                enemigo.vida -= 30
                time.sleep(1)
                print(f'la vida del enemigo ahora es: {enemigo.vida}')
                
        elif eleccion == "flechazo sangriento / plus" or eleccion == ' flechazo / plus':
            arco.flechazo_sangriento()
            actualizador = True
            if arco.flechazo_sangriento() == True:
                enemigo.vida -= 45
                time.sleep(1)
                print(f'la vida del enemigo ahora es: {enemigo.vida}')
        else:
            print("no has hecho ningun ataque")
        

        if actualizador == True:
            print("ok")
            time.sleep(1)
            print('ok')
            time.sleep(1)
            print('ok')
            time.sleep(1)
            print(f"es el turno del {ogroo.nombre}")
            time.sleep(0.5)
            print(f"ahora le toca al {enemigo.nombre} atacar ")
            enemigo.garrotazo(self=ogroo)
            if enemigo.garrotazo(self=ogroo) == True:
                player.vida = player.vida - enemigo.ataque
                time.sleep(0.5)
                print(f"ahora tu vida es: {player.mostrar_vida()}")
                actualizador = False
        
        if enemigo.vida <= 0:
            time.sleep(1)
            print("Bien le ganaste al ogro !!! \n tu vida esta con una mejora ahora tu vida es 140 :)")
            time.sleep(1)
            print("mejoraste de nivel a nivel 3")
            ganaste(True)
            break;

        elif player.vida <= 0:
            time.sleep(1)
            print('perdiste... \n pero aun es muy temprano para perder')
            player.restablecer_vida(player)
            enemigo.restablecer_vida(enemigo)
            ganaste(False)


if decicion == 'izquierda' or decicion == " izquierda":
    time.sleep(1)
    print("has elegido la izquierda \n y ahora te toca enfrentarte contra un ogro ¯ \ _ (ツ) _ / ¯ ")
    time.sleep(1)
    eleccion = input("quieres ver las caracteristicas del ogro si/no")
    if eleccion == "si" or eleccion == " si":
        #ogro = ogroo("ogro", 115, 30)
        time.sleep(1)
        print(ogroo.InformacionOgroo(self=ogroo))
        batalla_ogro(player, ogroo)
    else:
        batalla_ogro(player, ogroo)

elif decicion == "derecha" or decicion == " derecha":
    time.sleep(1)
    print("elegiste bien!!! te encontraste un arco")
    arco = arcoo()
    time.sleep(1)
    print("pero te encuentras con un ogro...")
    time.sleep(1)
    eleccion = input("quieres ver las caracteristicas del ogro si/no")

    if eleccion == "si" or eleccion == " si":
        #ogro = ogroo("ogro", 115, 30)
        print(ogroo.InformacionOgroo(self=ogroo))
        time.sleep(1)

        batalla__ogro_arco(player, ogroo)

    else:
        batalla__ogro_arco(player, ogroo)
        

else:
    print("no has elegido ningun camino \n pero... \n intentalo de nuevo ")
    decicion = input("izquierda o derecha")
    decicion = input("izquierda o derecha")
    decicion = input("izquierda o derecha")

print("y al final del dia terminaste con tu mision")
time.sleep(1)
print('mejoraste de nivel a nivel 3')
time.sleep(1)
player.subir_nivel(3)
print(f"tu nivel ahora es: {player.nivel}")

print("fin del capitulo 1")
time.sleep(1)
print("continuara")
time.sleep(2)
print(".")
time.sleep(2)
print('.')
time.sleep(2)
print('.')


