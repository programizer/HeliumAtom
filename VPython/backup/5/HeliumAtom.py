# from math import *
# from visual import *
# from visual.graph import * 
from vpython import *
# import vpython

scene.fullscreen = True

k = 8.988*10**9

spheres = [
sphere(pos=vector(0,0,0),radius =0.6*10**(-15),color=color.red,charge=2*1.6*10**(-19),mass=4*1.67*10**(-27),velocity=vector(0,0,0),a = vector(0,0,0),trail=curve(color=color.red)),
sphere(pos=vector(0,10*10**(-10),0),radius=0.2*10**(-90),color=color.blue,charge=-1*1.6*10**(-19),mass=9.1*10**(-31),velocity=vector(1*10**6,0,0),a=vector(0,0,0),trail=curve(color=color.blue)),
#sphere(pos=vector(0,12,0),radius=.08,color=color.green,mass=sqrt(4),velocity=vector(1.2,0,0.6),a=vector(0,0,0),trail=curve(color=color.green)),
sphere(pos=vector(0,5*10**(-10),0),radius=0.2*10**(-90),color=color.white,charge=-1*1.6*10**(-19),mass=9.1*10**(-31),velocity=vector(1.5*10**6,0,0.4*10**6),a=vector(0,0,0),trail=curve(color=color.white)),
#sphere(pos=vector(0,28,0),radius=.4,color=color.orange,mass=sqrt(80),velocity=vector(0.7,0,0.4),a=vector(0,0,0),trail=curve(color=color.orange)),
#sphere(pos=vector(0,32,0),radius=0.2,color=color.white,mass=-sqrt(10),velocity=vector(1.5,0,0.4),a=vector(0,0,0),trail=curve(color=color.white))
]


#print(spheres[0].a)

#print(len(spheres))


def acceleration1on2(sphere2,sphere1):
    r = sphere2.pos - sphere1.pos
    r_mag = mag(r)
    normal_r = norm(r)
    g = ((k*sphere1.charge*sphere2.charge)/pow(r_mag,2))/sphere2.mass*normal_r
    #print(g)
    return g
    
    
t = 0
dt = .01*10**(-7)
while 1:
    rate(100)
    for i in spheres:
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
        
            
    scene.center=vector(spheres[0].pos.x,spheres[0].pos.y,spheres[0].pos.z)


                
    # print(i.a)