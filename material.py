class Material(object):


  def __init__(self, diffuse, albedo, spec, refractive_index=0):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec
    self.refractive_index = refractive_index

  def __repr__(self):
    return f"Color {self.diffuse}, Albedo {self.albedo}, Spec {self.spec}, Refractive index {self.refractive_index}"
