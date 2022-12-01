from triangle import Triangle


class Pyramid(object):

  def __init__(self, vertices, material):
    self.vertices = vertices
    self.material = material
    self.triangles = self.__get_pyramid_triangles()

  
  def __get_pyramid_triangles(self):
    first_vertex, second_vertex, third_vertex, fourth_vertex = self.vertices
    first_triangle = Triangle((first_vertex, second_vertex, third_vertex), self.material)
    second_triangle = Triangle((first_vertex, second_vertex, fourth_vertex), self.material)
    third_triangle = Triangle((first_vertex, fourth_vertex, third_vertex), self.material)
    fourth_triangle = Triangle((second_vertex, fourth_vertex, third_vertex), self.material)
    return first_triangle, second_triangle, third_triangle, fourth_triangle

  
  def ray_interception(self, origin, direction):

    
    max_t_value = 999_999
    actual_intersect = None

    
    for triangle in self.triangles:

      
      triangle_intersect = triangle.ray_interception(origin, direction)

      
      if ((triangle_intersect is not None) and (triangle_intersect.distance < max_t_value)):
        max_t_value = triangle_intersect.distance
        actual_intersect = triangle_intersect

    
    return actual_intersect
