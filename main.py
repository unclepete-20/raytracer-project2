from raytracer import Raytracer
from vector import V3
from sphere import Sphere
from plane import Plane
from cube import Cube
from triangle import Triangle
from pyramid import Pyramid
from material import Material
from light import Light
from color import Color
from envmap import Envmap
import time


# Materials for raytracer
stone = Material(Color(100, 100, 100), [0.9, 0.1, 0, 0], 10)
skin = Material(Color(255, 219, 172), [0.7, 0.3, 0, 0], 150)
shirt = Material(Color(255, 255, 255), [0.6, 0.4, 0, 0], 200)
pants = Material(Color(66, 93, 140), [0.6, 0.4, 0, 0], 200)
cap = Material(Color(0, 255, 17), [0.6, 0.4, 0, 0], 200)
crystal_purple = Material(Color(35, 10, 45), [0.7, 0.3, 0.2, 0], 1500)
black_plastic = Material(Color(1, 1, 1), [0.9, 0.1, 0, 0], 32)
sun = Material(Color(236,195,15), [0.9, 0.1, 0, 0], 32)
window = Material(Color(135, 206, 235), [0.7, 0.3, 0.2, 0], 1200)
concrete = Material(Color(150, 150, 150), [0.9, 0.1, 0, 0], 0)
gold = Material(Color(204, 164, 61), [0.34615, 0.3143, 0.0903, 1.0], 20)


raytracer = Raytracer(1000, 1000)
raytracer.background_color = Color(0, 190, 255)
raytracer.light = Light(V3(5, -5, 5), 25, Color(255, 255, 255))
raytracer.set_ray_probability(1)


raytracer.scene = [
  
  #LAS VEGAS REFERENCE
  
  # Surface area
  Plane(V3(0, 2, -5), 12, 12, stone),

  # Pyramid
  Pyramid(((-6, 3, -10), (1, 3, -10), (-2.25, -1, -9), (-2.25, 3, -8)), crystal_purple),
  
  # Sun
  Sphere(V3(-6, -5.5, -15), 0.5, sun),
  
  # Sculpture
  Sphere(V3(1.25, 1.8, -4), 0.2, gold),
  Sphere(V3(1.50, 1.8, -4), 0.2, gold),
  Sphere(V3(1.40, 1.5, -4), 0.2, gold),
  
  # Person on scene
  Cube(V3(-2.25, 1.8, -5), 0.35, black_plastic),
  Cube(V3(-2.25, 1.45, -5), 0.35, pants),
  Cube(V3(-2.25, 1.1, -5), 0.35, shirt),
  Cube(V3(-2.25, 0.7, -5), 0.35, skin),
  Cube(V3(-2.75, 1.1, -5), 0.35, skin),
  Cube(V3(-2, 1.1, -5), 0.35, skin),
  Cube(V3(-2.25, 0.4, -5), 0.35, cap),
  
  

  
  # Building 
  Cube(V3(1, 1.75, -8), 0.5, concrete),
  Cube(V3(1, 1.25, -8), 0.5, concrete),
  Cube(V3(1, 0.75, -8), 0.5, concrete),
  Cube(V3(1, 0.25, -8), 0.5, concrete),
  Cube(V3(1, -0.25, -8), 0.5, concrete),
  Cube(V3(1.5, 1.75, -8), 0.5, concrete),
  Cube(V3(2, 1.75, -8), 0.5, concrete),
  Cube(V3(2.5, 1.75, -8), 0.5, concrete),
  Cube(V3(1.5, -0.25, -8), 0.5, concrete),
  Cube(V3(2, -0.25, -8), 0.5, concrete),
  Cube(V3(2.5, -0.25, -8), 0.5, concrete),
  Cube(V3(2.5, 1.25, -8), 0.5, concrete),
  Cube(V3(2.5, 0.75, -8), 0.5, concrete),
  Cube(V3(2.5, 0.25, -8), 0.5, concrete),
  Cube(V3(1.5, 1.25, -8), 0.5, window),
  Cube(V3(1.5, 0.75, -8), 0.5, concrete),
  Cube(V3(1.5, 0.25, -8), 0.5, window),
  Cube(V3(2, 1.25, -8), 0.5, concrete),
  Cube(V3(2, 0.75, -8), 0.5, window),
  Cube(V3(2, 0.25, -8), 0.5, concrete),
  Cube(V3(1, 1.75*4, -8), 0.5, black_plastic),
  Cube(V3(1, 1.25*4, -8), 0.5, black_plastic),
  Cube(V3(1, 0.75*4, -8), 0.5, black_plastic),
  Cube(V3(1, 0.25*4, -8), 0.5, black_plastic),
  Cube(V3(1, -0.25*4, -8), 0.5, black_plastic),
  Cube(V3(1.5, 1.75*4, -8), 0.5, black_plastic),
  Cube(V3(2, 1.75*4, -8), 0.5, black_plastic),
  Cube(V3(2.5, 1.75*4, -8), 0.5, black_plastic),
  Cube(V3(1.5, -0.25*4, -8), 0.5, black_plastic),
  Cube(V3(2, -0.25*4, -8), 0.5, black_plastic),
  Cube(V3(2.5, -0.25*4, -8), 0.5, black_plastic),
  Cube(V3(2.5, 1.25*4, -8), 0.5, black_plastic),
  Cube(V3(2.5, 0.75*4, -8), 0.5, black_plastic),
  Cube(V3(2.5, 0.25*4, -8), 0.5, black_plastic),
  Cube(V3(1.5, 1.25*4, -8), 0.5, window),
  Cube(V3(1.5, 0.75*4, -8), 0.5, concrete),
  Cube(V3(1.5, 0.25*4, -8), 0.5, window),
  Cube(V3(2, 1.25*4, -8), 0.5, concrete),
  Cube(V3(2, 0.75*4, -8), 0.5, window),
  Cube(V3(2, 0.25*4, -8), 0.5, concrete),
  
]

raytracer.set_envmap(Envmap("./env/sky.bmp"))


start = time.time()
raytracer.render()
raytracer.write("proyecto2.bmp")
print(f"\nThe Raytracer has finished rendering in {round((time.time() - start), 4)} seconds approximately!\n")
