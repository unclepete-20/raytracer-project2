import bmp
import math


class Envmap(object):


  def __init__(self, path):
    self.path = path
    self.width, self.height, self.pixels = bmp.read_bmp(path)

  
  def get_color(self, direction):

    normalized_direction = direction.norm()
    x = round(((math.atan2(normalized_direction.z, normalized_direction.x) / (2 * math.pi)) + 0.5) * self.width)
    y = (-1 * round((math.acos((-1 * normalized_direction.y)) / math.pi) * self.height))

    x -= 1 if (x > 0) else 0
    y -= 1 if (y > 0) else 0

    return self.pixels[y][x]
