#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine 
pilas = pilasengine.iniciar()
#agregando el personaje 
runner = pilas.actores.Shaolin()
runner.x = -500
runner.y = -500
runner.escala = 0.2
runner.aprender("LimitadoABordesDePantalla")

