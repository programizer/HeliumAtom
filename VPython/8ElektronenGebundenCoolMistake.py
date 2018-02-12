# from math import *
# from visual import *
# from visual.graph import * 
from vpython import *
# import vpython

scene.fullscreen = True

G = 1

spheres = [
sphere(pos=vector(0,0,0),radius =0.6,color=color.red,charge=8*2,mass=4*7200,velocity=vector(0,0,0),a = vector(0,0,0),trail=curve(color=color.red)),
sphere(pos=vector(20,0,0),radius=0.2,color=color.blue,charge=-1,mass=1,velocity=vector(0,0.75,0),a=vector(0,0,0),trail=curve(color=color.blue)),
#sphere(pos=vector(0,12,0),radius=.08,color=color.green,mass=sqrt(4),velocity=vector(1.2,0,0.6),a=vector(0,0,0),trail=curve(color=color.green)),
sphere(pos=vector(-20,0,0),radius=0.2,color=color.blue,charge=-1,mass=1,velocity=vector(0,-0.75,0),a=vector(0,0,0),trail=curve(color=color.blue)),
sphere(pos=vector(0,20,0),radius=0.2,color=color.blue,charge=-1,mass=1,velocity=vector(-0.75,0,0),a=vector(0,0,0),trail=curve(color=color.blue)),
sphere(pos=vector(0,-20,0),radius=0.2,color=color.blue,charge=-1,mass=1,velocity=vector(0.75,0,0),a=vector(0,0,0),trail=curve(color=color.blue)),
sphere(pos=vector(10*sqrt(2),10*sqrt(2),0),radius=0.2,color=color.white,charge=-1,mass=1,velocity=vector(3*sqrt(2)/8,-3*sqrt(2)/8,0),a=vector(0,0,0),trail=curve(color=color.white)),
sphere(pos=vector(10*sqrt(2),-10*sqrt(2),0),radius=0.2,color=color.white,charge=-1,mass=1,velocity=vector(-3*sqrt(2)/8,-3*sqrt(2)/8,0),a=vector(0,0,0),trail=curve(color=color.white)),
sphere(pos=vector(-10*sqrt(2),10*sqrt(2),0),radius=0.2,color=color.white,charge=-1,mass=1,velocity=vector(3*sqrt(2)/8,3*sqrt(2)/8,0),a=vector(0,0,0),trail=curve(color=color.white)),
sphere(pos=vector(-10*sqrt(2),-10*sqrt(2),0),radius=0.2,color=color.white,charge=-1,mass=1,velocity=vector(-3*sqrt(2)/8,3*sqrt(2)/8,0),a=vector(0,0,0),trail=curve(color=color.white))
]


#print(spheres[0].a)

#print(len(spheres))


def acceleration1on2(sphere2,sphere1):
    r = sphere2.pos - sphere1.pos
    r_mag = mag(r)
    normal_r = norm(r)
    g = ((G*sphere1.charge*sphere2.charge)/pow(r_mag,2))/sphere2.mass*normal_r
    #if (r_mag<0.1):
    #    g = - 2 * sphere2.velocity
    #if (mag(g)>100):
    #    g=10*norm(g)
    #print(g)
    return g
    
    
t = 0
dt = .01
while 1:
    rate(100)
    #dt=min(.01/mag(spheres[1].velocity),.01/mag(spheres[2].velocity))
    #sleep(dt)
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