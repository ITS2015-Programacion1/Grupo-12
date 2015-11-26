
#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine 
pilas = pilasengine.iniciar()
import random
import math 
#variables 
balas_simples = pilas.actores.Misil

#mapa
mapa_desde_archivo=pilas.actores.MapaTiled("mapa_plataformas.tmx")

# creando el personaje principal
class  Runner(pilasengine.actores.Actor):
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
runner.escala=0.09
runner.aprender("SeMantieneEnPantalla")

#agregando habilidades 
class MirarActor (pilasengine.habilidades.Habilidad):

                    def iniciar(self, receptor, actor_perseguido, velocidad=1):    
                        self.receptor = receptor
                        self.actor_perseguido = actor_perseguido
                        self.velocidad = velocidad
        
                    def actualizar(self):
                        self.receptor.rotacion=135
                        self.receptor.disparar
                         
                    
#enemigo1                    
pilas.habilidades.vincular(MirarActor)
enemigo1 = pilas.actores.Torreta()
enemigo1.x = 164
enemigo1.y = 116
enemigo1.aprender(pilas.habilidad.Disparar,grupo_ enemigos= runner, cuando_elimina_enemigo=perder_fin)
enemigo1.eliminar_habilidad("rotarconmouse")   
enemigo1.aprender("MirarActor", actor_perseguido = runner)                                                    
enemigo1.municion=pilasengine.actores.Misil

#enemigo2
enemigo2 = pilas.actores.Torreta()
enemigo2.x = -307
enemigo2.y = 227
enemigo2.aprender("Disparar")
enemigo2.eliminar_habilidad("rotarconmouse")                                                     
enemigo2.municion=pilasengine.actores.Misil
enemigo2.rotacion=225
#creando las funciones 
def perder_fin(runner, balas_simples):
    runner.eliminar()
    balas_simples.eliminar()
    pilas.camara.vibrar(intensidad=2, tiempo=3)
    global fin_del_juego

def actor_destruido(disparo, runner):
    runner.eliminar()
    disparo.eliminar()
    


     
#creando las colisiones del juego 

pilas.ejecutar()
