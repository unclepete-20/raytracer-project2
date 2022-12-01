from color import Color
from vector import V3
import struct


BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
GREEN = Color(0, 255, 0)
BLUE = Color(0, 0, 255)
ORANGE = Color(225, 135, 65)


def char(c):
  # 1 byte
  return struct.pack('=c',c.encode('ascii'))

def word(w):
  # 2  bytes
  return struct.pack('=h',w)

def dword(d):
  #4 bytes
  return struct.pack('=l', d)

def color(r, g, b):
    return bytes([round(b),round(g),round(r)])


reflect = lambda I, N: (I - N * 2 * (N @ I)).norm()
unpack = lambda buffer: struct.unpack("=l", buffer)[0]


def refract(I, N, roi):


  eta_i = 1
  eta_t = roi

  
  cos_i = ((I @ N) * -1)

  
  if (cos_i < 0):
    cos_i *= -1
    eta_i *= -1
    eta_t *= -1
    N *= -1

  
  eta_t = 1E-06 if (eta_t == 0) else eta_t
  eta = (eta_i / eta_t)

  
  k = (1 - ((eta ** 2) * (1 - (cos_i ** 2))))

  
  if (k < 0):
    return V3(0, 0, 0)

  
  cos_t = (k ** 0.5)

  
  return ((I * eta) + (N * ((eta * cos_i) - cos_t))).norm()
