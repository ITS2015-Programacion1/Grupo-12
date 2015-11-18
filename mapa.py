import pilasengine
import random


pilas=pilasengine.iniciar()

mapa=pilas.actores.MapaTiled("juego_plataformas.tmx")

pilas.ejecutar()
