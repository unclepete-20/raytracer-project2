from intersect import Intersect


class Sphere(object):

  
  def __init__(self, center, radius, material):
    self.center = center
    self.radius = radius
    self.material = material

  
  def ray_interception(self, origin, direction):

    
    L = self.center - origin
    tca = L @ direction
    l = L.length()
    d2 = ((l ** 2) - (tca ** 2))
    squared_radius = (self.radius ** 2)


    if (d2 > squared_radius):
      return None

    
    thc = ((squared_radius - d2) ** 0.5)
    t0 = (tca - thc)
    t1 = (tca + thc)

    
    t0 = t1 if (t0 < 0) else t0

    
    hit_point = ((direction * t0) + origin)
    normal = (hit_point - self.center).norm()

    
    return Intersect(t0, hit_point, normal) if (t0 > 0) else None

  
  def __repr__(self):
    return f"({self.center}, {self.radius})"
