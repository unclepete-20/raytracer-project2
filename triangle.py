from intersect import Intersect
from vector import V3

class Triangle(object):

  
  def __init__(self, vertices, material):
    self.vertices = vertices
    self.individual_vertices = self.__get_individual_vertices()
    self.material = material

  
  def __get_individual_vertices(self):
    vertices = []
    for vertex in self.vertices:
      individual_vertex = V3(*vertex)
      vertices.append(individual_vertex)
    return vertices

  
  def ray_interception(self, origin, direction):

    
    first_vertex, second_vertex, third_vertex = self.individual_vertices

    
    first_edge = (second_vertex - first_vertex)
    second_edge = (third_vertex - first_vertex)

    
    rel_height = (direction * second_edge)
    tilt = (first_edge @ rel_height)

    
    if (-1E-06 < tilt < 1E-06):
      return None

    
    inverse_tilt = (1 / tilt)
    u = inverse_tilt * ((origin - first_vertex) @ rel_height)

    
    if ((u < 0) or (u > 1)):
      return None

    
    qvec = ((origin - first_vertex) * first_edge)
    v = inverse_tilt * (direction @ qvec)

    
    if ((v < 0) or ((u + v) > 1)):
      return None

    
    tvec = inverse_tilt * (second_edge @ qvec)

    
    if (tvec > 1E-06):

      
      hit_point = (origin + (direction * tvec))
      normal = (first_edge * second_edge).norm()

      
      return Intersect(
        distance=tvec,
        hit_point=hit_point,
        normal=normal,
      )

    
    else:
      return None
