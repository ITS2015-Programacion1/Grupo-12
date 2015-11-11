import pilasengine
import random


pilas=pilasengine.iniciar()
pilas.fondos.Selva()

def iniciar_juego():
    print "Tengo que iniciar el juego"

def salir_del_juego():
    print "Tengo que salir..."

def controles():
    print "muestro los controles"

pilas.actores.Menu(
        [
            ('iniciar juego', iniciar_juego),
            ("controles",controles),
            ('salir', salir_del_juego),
        ])

pilas.ejecutar()
