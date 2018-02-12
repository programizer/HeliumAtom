

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 23:16:24 2014

@author: steven
"""

from math import *
# from visual import *
# from visual.graph import * 
# from vpython import *
import vpython

scene.fullscreen = true

G = 5

spheres = [
sphere(pos=(0,0,0),radius =0.6,color=color.yellow,mass=200,velocity=vector(0,0,0),a = vector(0,0,0),trail=curve(color=color.yellow)),
sphere(pos=(0,10,0),radius=0.2,color=color.blue,mass=10,velocity=vector(10,0,0),a=vector(0,0,0),trail=curve(color=color.blue)),
sphere(pos=(0,12,0),radius=.08,color=color.green,mass=4,velocity=vector(12,0,6),a=vector(0,0,0),trail=curve(color=color.green)),
sphere(pos=(0,5,0),radius=0.2,color=color.red,mass=8,velocity=vector(15,0,4),a=vector(0,0,0),trail=curve(color=color.red)),
sphere(pos=(0,28,0),radius=.4,color=color.orange,mass=80,velocity=vector(7,0,4),a=vector(0,0,0),trail=curve(color=color.orange)),
sphere(pos=(0,32,0),radius=0.2,color=color.white,mass=10,velocity=vector(15,0,4),a=vector(0,0,0),trail=curve(color=color.white))
]


#print(spheres[0].a)

#print(len(spheres))


def acceleration1on2(sphere2,sphere1):
    r = sphere2.pos - sphere1.pos
    r_mag = mag(r)
    normal_r = norm(r)
    g = -((G*sphere1.mass)/pow(r_mag,2))*normal_r
    #print(g)
    return g
    
    
t = 0
dt = .01
while 1:
    rate(100)
    for n in spheres:
        i.a = vector(0,0,0)
        soi = vector(0,0,0)
        for j in spheres:
            if i!=j:
                i.a = i.a + acceleration1on2(i,j)
            
          
                

                
    for i in spheres:
        #print(i.velocity)
        i.velocity = i.velocity + i.a *dt
        i.pos = i.pos+i.velocity*dt
        #print(i.a)
        i.trail.append(pos=i.pos)
        
            
    scene.center=(spheres[0].pos.x,spheres[0].pos.y,spheres[0].pos.z)


                
    #print(i.a)
               