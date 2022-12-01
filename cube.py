
from intersect import Intersect


class Cube(object):
  
  def __init__(self, center, width, material):
    self.center = center
    self.width = width
    self.material = material
    self.COMPONENTS = 3

  
  def ray_interception(self, origin, direction):

    
    min_t_value = -999_999
    max_t_value = 999_999

    
    for i in range(self.COMPONENTS):

      
      if (direction.values[i] != 0):
        min_tc_value = (((self.center.values[i] - (self.width / 2)) - origin.values[i]) / direction.values[i])
        max_tc_value = (((self.center.values[i] + (self.width / 2)) - origin.values[i]) / direction.values[i])
      else:
        min_tc_value = -999_999
        max_tc_value = 999_999

      
      if (min_tc_value > max_tc_value):
        min_tc_value, max_tc_value = max_tc_value, min_tc_value

      
      min_t_value = min_tc_value if (min_tc_value > min_t_value) else min_t_value
      max_t_value = max_tc_value if (max_tc_value < max_t_value) else max_t_value

      
      if (min_t_value > max_t_value):
        return None

    
    if (min_t_value < 0):
      min_t_value = max_t_value

      
      if (min_t_value < 0):
        return None

    
    hit_point = ((direction * min_t_value) - origin)
    normal = (hit_point - self.center).norm()

    
    return Intersect(distance=min_t_value, hit_point=hit_point, normal=normal)
