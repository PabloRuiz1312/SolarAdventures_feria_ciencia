import pygame
class misiones:
    def misionPrincipal(primeraMision,mapa,luna,estadoInicial,flecha):
        teclaPulsada = pygame.key.get_pressed()
        if(mapa==True):
            primeraMision=True
            if(teclaPulsada[pygame.K_RETURN] and (flecha.rect.x>500 and flecha.rect.x<515)):
                luna = True
                estadoInicial = False
        else:
            primeraMision=False
        return luna,primeraMision,estadoInicial
    def misionLuna(segundaMision,cogerPropulsor,mapa,marte,flecha,luna,puntos):
        teclaPulsada = pygame.key.get_pressed()
        if(cogerPropulsor==True):
            segundaMision=True
            if(teclaPulsada[pygame.K_RETURN] and (flecha.rect.x>450 and flecha.rect.x<480) and mapa==True):
                marte = True
                luna = False
                puntos+=300
        return marte,luna,segundaMision,puntos

    def construirGenerador(screen,protagonista,volverNave,escena3,generadorAgua,mostrar,generador,piezas):
        teclaPulsada = pygame.key.get_pressed()
        if(piezas>=4 and volverNave==True and escena3==True): 
            if(protagonista.rect.x>191 and protagonista.rect.x<499 and protagonista.rect.y>540 and escena3==True):
                if(teclaPulsada[pygame.K_e] and generadorAgua==False):
                    mostrar=True
                if(teclaPulsada[pygame.K_RETURN] and mostrar==True):
                    generadorAgua=True
                    piezas-=4
                    mostrar=False
                if(mostrar):
                    generador.draw(screen)
        return generadorAgua,mostrar,piezas
    def misionMarte(terceraMision,generadorAgua,mapa,jupiter,flecha,marte,puntos):
        teclaPulsada = pygame.key.get_pressed()
        if(generadorAgua):
            terceraMision=True
            if(teclaPulsada[pygame.K_RETURN] and (flecha.rect.x>290 and flecha.rect.x<350) and mapa==True):
                jupiter=True
                marte=False
                puntos+=300
        return jupiter,marte,terceraMision,puntos
    
    def misionJupiter(cuartaMision,flecha,volverNave,cristal,distribuidor,mapa,jupiter,urano,puntos):
        teclaPulsada = pygame.key.get_pressed()
        if(cristal==False and distribuidor==False and volverNave==True):
            cuartaMision=True
            if(teclaPulsada[pygame.K_RETURN] and (flecha.rect.x>110 and flecha.rect.x<130) and mapa==True):
                urano=True
                jupiter=False
                puntos+=300
        elif(cristal==False and distribuidor==True and volverNave==True):
            cuartaMision=True
            if(teclaPulsada[pygame.K_RETURN] and (flecha.rect.x>110 and flecha.rect.x<130) and mapa==True):
                urano=True
                jupiter=False
                puntos+=300
        return cuartaMision,jupiter,urano,puntos
    
    def misionUrano(quintaMision,flecha,volverNave,trajeAP,mapa,urano,pluton,puntos):
        teclaPulsada = pygame.key.get_pressed()
        if(trajeAP==True):
            quintaMision=True
        if(mapa and quintaMision):
            if(teclaPulsada[pygame.K_RETURN] and (flecha.rect.x>5 and flecha.rect.x<17) and mapa==True):
                pluton=True
                urano=False
                puntos+=300
        return quintaMision,urano,pluton,puntos