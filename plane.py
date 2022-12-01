from intersect import Intersect
from vector import V3

class Plane(object):

  def __init__(self, center, width, length, material):
    self.center = center
    self.width = width
    self.length = length
    self.material = material

  
  def ray_interception(self, origin, direction):

    
    direction.y = 1E-06 if (direction.y == 0) else direction.y
    distance = (((self.center.y - origin.y)) / direction.y)
    hit_point = ((direction * distance) - origin)
    normal = V3(0, -1, 0)

    
    neg_distance = (distance <= 0)
    too_left = (hit_point.x < (self.center.x - (self.width / 2)))
    too_right = (hit_point.x > (self.center.x + (self.width / 2)))
    too_close = (hit_point.z < (self.center.z - (self.length / 2)))
    too_far = (hit_point.z > (self.center.z + (self.length / 2)))

    
    if ((neg_distance) or (too_right) or (too_left) or (too_far) or (too_close)):
      return None

    
    return Intersect(distance, hit_point, normal)

  
  def __repr__(self):
    return f"({self.center}, {self.width}, {self.length})"
