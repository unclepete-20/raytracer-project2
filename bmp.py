
from color import Color
import utils


def write_bmp(filename, framebuffer, width, height):
  
  # BMP FILE BYTES TO PROCESS IT
  FILE_HEADER_SIZE = 14
  IMAGE_HEADER_SIZE = 40
  HEADER_SIZE = (FILE_HEADER_SIZE + IMAGE_HEADER_SIZE)
  COLORS_PER_PIXEL = 3
  

  file = open(filename, "bw")

  
  file.write(utils.char("B"))
  file.write(utils.char("M"))
  file.write(utils.dword(HEADER_SIZE + (width * height * COLORS_PER_PIXEL)))
  file.write(utils.dword(0))
  file.write(utils.dword(HEADER_SIZE))

  
  file.write(utils.dword(IMAGE_HEADER_SIZE))
  file.write(utils.dword(width))
  file.write(utils.dword(height))
  file.write(utils.word(1))
  file.write(utils.word(24))
  file.write(utils.dword(0))
  file.write(utils.dword(width * height * COLORS_PER_PIXEL))
  file.write(utils.dword(0))
  file.write(utils.dword(0))
  file.write(utils.dword(0))
  file.write(utils.dword(0))

  
  for x in range(width):
    for y in range(height):
      file.write(framebuffer[y][x].to_bytes())

  
  file.close()


def read_bmp(path):

  
  with open(path, "rb") as image:

    
    image.seek(2 + 4 + 2 + 2)
    header_size = utils.unpack(image.read(4))
    image.seek(2 + 4 + 2 + 2 + 4 + 4)
    width = utils.unpack(image.read(4))
    height = utils.unpack(image.read(4))

    
    image.seek(header_size)

    
    pixels = []

    
    for y in range(height):

      
      pixels.append([])

      
      for _ in range(width):

        
        b, g, r = (ord(image.read(1)), ord(image.read(1)), ord(image.read(1)))

        
        pixels[y].append(Color(r, g, b))

  
  return width, height, pixels
