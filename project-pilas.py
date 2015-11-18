
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine 
pilas = pilasengine.iniciar()
import random
import math 
#agregando el personaje
mapa_desde_archivo=pilas.actores.MapaTiled("mapa_plataformas.tmx")
def salir():
    exit()
def iniciar_juego():
    menu.x=1445252345234 
    class Runner(pilasengine.actores.Actor):
        def iniciar(self):
            self.imagen = "runner.png"
            self.figura = pilas.fisica.Circulo(self.x, self.y, 17,friccion=0, restitucion=0)
            self.figura.sin_rotacion = True
            self.figura.escala_de_gravedad = 2
            self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 20, 5, sensor=True, dinamica=False)

        def actualizar(self):
            velocidad = 10
            salto = 15
            self.x = self.figura.x
            self.y = self.figura.y
            if self.pilas.control.derecha:
                self.figura.velocidad_x = velocidad
                self.rotacion -= velocidad
            elif self.pilas.control.izquierda:
                self.figura.velocidad_x = -velocidad
           
            else:
                self.figura.velocidad_x = 0

            if self.esta_pisando_el_suelo():
                if self.pilas.control.arriba and int(self.figura.velocidad_y) <= 0:
                    self.figura.impulsar(0, salto)

            self.sensor_pies.x = self.x
            self.sensor_pies.y = self.y - 20            
    
        def esta_pisando_el_suelo(self):
            return len(self.sensor_pies.figuras_en_contacto) > 0
    runner = Runner(pilas)
    runner.aprender("MoverseConelTeclado")
    runner.escala=0.1
    runner.aprender("SeMantieneEnPantalla")


    class MirarActor (pilasengine.habilidades.Habilidad):

                    def iniciar(self, receptor, actor_perseguido, velocidad=1):    
                        self.receptor = receptor
                        self.actor_perseguido = actor_perseguido
                        self.velocidad = velocidad
        
                    def actualizar(self):
                        x=self.actor_perseguido .x * -1
                        b = 221
                        h=math.sqrt(x*x+b*b)
                        salpha= (math.sin(90)*x)/h
                        alpha=math.asin(salpha)
                    
                        self.receptor.rotacion=(alpha)
                    
                    
                            

    #agregando las torretas al mapa
    ''' 
    class Torreta (pilasengine.actores.Actor):
        def iniciar(self):
            self.imagen= "torreta.png"
    torreta= Torreta(pilas)           
    '''

    pilas.habilidades.vincular(MirarActor)
    enemigo = pilas.actores.Torreta()
    enemigo.x = 300
    enemigo.y = 100
    enemigo.aprender("Disparar")
    enemigo.eliminar_habilidad("rotarconmouse")   
    enemigo.aprender("MirarActor", actor_perseguido = runner)                                                    
menu=pilas.actores.Menu([("INICIAR_JUEGO",iniciar_juego),("SALIR",salir)])

pilas.ejecutar()
