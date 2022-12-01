from light import Light
from color import Color
from vector import V3
import bmp
import math
import utils
import random


MAX_RECURSION_DEPTH = 3


class Raytracer(object):

  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.background_color = utils.BLACK
    self.current_color = utils.WHITE
    self.ray_probability = 1
    self.framebuffer = []
    self.scene = []
    self.colors = []
    self.envmap = None
    self.light = Light(V3(0, 0, 0), 1, Color(255, 255, 255))
    self.clear()

  
  def clear(self):
    self.framebuffer = [[self.background_color for _ in range(self.width)] for _ in range(self.height)]

  
  def set_background_color(self, r, g, b):
    self.background_color = Color(r, g, b)
  
  
  def set_current_color(self, r, g, b):
    self.current_color = Color(r, g, b)

  
  def point(self, x, y, color=None):
    if ((0 <= y <= self.height) and (0 <= x <= self.width)):
      self.framebuffer[y][x] = color or self.current_color

  
  def set_envmap(self, envmap):
    self.envmap = envmap

  
  def get_background(self, direction):
    return self.envmap.get_color(direction) if (self.envmap is not None) else self.background_color

  
  def cast_ray(self, origin, direction, recursion_counter=0):

    
    if (recursion_counter >= MAX_RECURSION_DEPTH):
      return self.get_background(direction)

    
    material, intersect = self.scene_intersect(origin, direction)

    
    if (material is None):
      return self.get_background(direction)

    
    light_direction = (self.light.position - intersect.hit_point).norm()

    
    shadow_bias = 1.1
    shadow_origin = (intersect.hit_point + (intersect.normal * shadow_bias))
    shadow_material, _ = self.scene_intersect(shadow_origin, light_direction)
    shadow_intensity = 0.75 if (shadow_material is not None) else 0

   
    diffuse_intensity = (light_direction @ intersect.normal)
    actual_diffuse = (material.diffuse * diffuse_intensity * material.albedo[0] * (1 - shadow_intensity))

    
    light_reflection = utils.reflect(light_direction, intersect.normal)
    reflection_intensity = max(0, (light_reflection @ direction))
    specular_intensity = (self.light.intensity * (reflection_intensity ** material.spec))

    
    specular_component = (self.light.color * specular_intensity * material.albedo[1])

    
    if (material.albedo[2] > 0):
      reflection_direction = utils.reflect(direction, intersect.normal)
      reflection_bias = -0.5 if ((reflection_direction @ intersect.normal) < 0) else 0.5
      reflection_origin = (intersect.hit_point + (intersect.normal * reflection_bias))
      reflection_color = self.cast_ray(reflection_origin, reflection_direction, (recursion_counter + 1))
    else:
      reflection_color = Color(0, 0, 0)

    
    if (material.albedo[3] > 0):
      refraction_direction = utils.refract(direction, intersect.normal, material.refractive_index)
      refraction_bias = -0.5 if ((refraction_direction @ intersect.normal) < 0) else 0.5
      refraction_origin = (intersect.hit_point + (intersect.normal * refraction_bias))
      refract_color = self.cast_ray(refraction_origin, refraction_direction, (recursion_counter + 1))
    else:
      refract_color = Color(0, 0, 0)

    
    reflection = (reflection_color * material.albedo[2])
    refraction = (refract_color * material.albedo[3])

    
    return (actual_diffuse + specular_component + reflection + refraction)

  
  def scene_intersect(self, origin, direction):

    
    z_buffer = 999_999
    material = None
    intersect = None

    
    for object in self.scene:

      
      object_intersect = object.ray_interception(origin, direction)

      
      if (object_intersect and (object_intersect.distance < z_buffer)):

        
        z_buffer = object_intersect.distance
        material = object.material
        intersect = object_intersect

    
    return material, intersect

  
  def set_ray_probability(self, ray_probability):
    self.ray_probability = ray_probability

  
  def render(self):

    
    aspect_ratio = (self.width / self.height)
    field_of_view = int(math.pi / 2)
    tangent = math.tan(field_of_view / 2)

    
    for y in range(self.height):
      for x in range(self.width):

        
        random_value = random.random()

        
        if (random_value <= self.ray_probability):
          i = ((((2 * (x + 0.5)) / self.width) - 1) * (tangent * aspect_ratio))
          j = ((1 - ((2 * (y + 0.5)) / self.height)) * tangent)
          origin = V3(0, 0, 0)
          direction = V3(i, j, -1).norm()
          color = self.cast_ray(origin, direction)
          self.point(y, x, color)

  
  def write(self, filename):
    return bmp.write_bmp(filename, self.framebuffer, self.width, self.height)
