class sword():
    remolino_o = 20
    ataque_normal_o = 30
    especial_o = 45
    #una lista con los ataque para mejorar
    lista_ataques = [
        [remolino_o],
        [ataque_normal_o],
        [especial_o]
    ]
    
    #funcion remolino
    def remolino(self):
        return True
    
    #funcion del ataque normal
    def ataque_normal(self):
        return True
    
    #funcion del ataque especial
    def especial(self):
        return True
    
    #funcion para ver los ataque disponible
    def ver_habilidades(self):
        lista_habilidades = [
            ["tienes remolino"],
            ["tienes un ataque normal"],
            ["y tienes un ataque especial"]
        ]
        for i in lista_habilidades:
            for j in i:
                return j