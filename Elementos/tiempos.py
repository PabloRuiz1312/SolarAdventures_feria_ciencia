import pygame
class sistemaTiempo:

    def tiempoEnNivel(tiempo,contMinutos,screen):
        frasePuntos = pygame.font.Font(None,80)
        blanco = pygame.Color(255,255,255)
        fraseTiempo = "TIEMPO "+str(contMinutos)+":"+str(int(tiempo/1000))
        transmitir = frasePuntos.render(fraseTiempo,1,blanco)
        screen.blit(transmitir,(20,880))
        tiempo+=2.5
        if(tiempo/1000>60):
            tiempo=0
            contMinutos+=1
        return tiempo,contMinutos
    def tiempoEnPlaneta(tiempo,contMinutos,screen):
        frasePuntos = pygame.font.Font(None,80)
        blanco = pygame.Color(255,255,255)
        fraseTiempo = "TIEMPO "+str(contMinutos)+":"+str(int(tiempo/1000))
        transmitir = frasePuntos.render(fraseTiempo,1,blanco)
        screen.blit(transmitir,(20,880))
        tiempo+=8.5
        if(tiempo/1000>60):
            tiempo=0
            contMinutos+=1
        return tiempo,contMinutos
    def contarTiempo(salirComienzo,salirControles,salirPuntos,salirNivelLuna,salirNivelMarte,salirNivelJupiter,salirNivelUrano,salirNivelPluton,tiempo,contMinutos,screen,luna,marte,jupiter,urano,pluton,faseInicial,gameOverVida,gameOverGasolina,gameOverArreglos,gameOverJupiter,vidaJefe):
        frasePuntos = pygame.font.Font(None,80)
        blanco = pygame.Color(255,255,255)
        if(salirComienzo==True and salirControles==True and salirPuntos==True):
            if(faseInicial==True):
                frasePuntos = pygame.font.Font(None,80)
                blanco = pygame.Color(255,255,255)
                fraseTiempo = "TIEMPO "+str(contMinutos)+":"+str(int(tiempo/1000))
                transmitir = frasePuntos.render(fraseTiempo,1,blanco)
                screen.blit(transmitir,(20,880))
                tiempo+=1
                if(tiempo/1000>60):
                    tiempo=0
                    contMinutos+=1
            if(salirNivelLuna==False and faseInicial==False and luna==True):
                tiempo,contMinutos = sistemaTiempo.tiempoEnNivel(tiempo,contMinutos,screen)
            elif(salirNivelMarte==False and luna==False and marte==True):
                tiempo,contMinutos = sistemaTiempo.tiempoEnNivel(tiempo,contMinutos,screen)
            elif(salirNivelJupiter==False and marte==False and jupiter==True):
                tiempo,contMinutos = sistemaTiempo.tiempoEnNivel(tiempo,contMinutos,screen)
            elif(salirNivelUrano==False and jupiter==False and urano==True):
                tiempo,contMinutos = sistemaTiempo.tiempoEnNivel(tiempo,contMinutos,screen)
            elif(salirNivelPluton==False and urano==False and pluton==True):
                tiempo,contMinutos = sistemaTiempo.tiempoEnNivel(tiempo,contMinutos,screen)
            elif(gameOverVida==True  or gameOverArreglos==True or gameOverGasolina==True or gameOverJupiter==True):
                tiempo,contMinutos = sistemaTiempo.tiempoEnNivel(tiempo,contMinutos,screen)
            elif(pluton==False and vidaJefe<=0):
                tiempo+=0
                fraseTiempo = "TIEMPO "+str(contMinutos)+":"+str(int(tiempo/1000))
                transmitir = frasePuntos.render(fraseTiempo,1,blanco)
                screen.blit(transmitir,(20,880))
            else:
                tiempo,contMinutos = sistemaTiempo.tiempoEnPlaneta(tiempo,contMinutos,screen)
        else:
            fraseTiempo = "TIEMPO "+str(contMinutos)+":"+str(int(tiempo/1000))
            transmitir = frasePuntos.render(fraseTiempo,1,blanco)
            screen.blit(transmitir,(20,880))
        return tiempo,contMinutos