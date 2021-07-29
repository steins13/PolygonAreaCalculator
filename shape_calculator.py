# from _typeshed import Self


class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, newWidth):
    self.width = newWidth

  def set_height(self, newHeight):
    self.height = newHeight

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return ((self.width ** 2) + (self.height ** 2)) ** 0.5

  def get_picture(self):
    wLine = ""
    hLine = ""
    width = self.width
    height = self.height

    if width > 50 or height > 50:
      return "Too big for picture."

    while height > 0:
      while width > 0:
        wLine = wLine + "*"
        width = width - 1
      wLine = wLine + "\n"
      hLine = hLine + wLine
      wLine = ""  
      width = self.width
      height = height - 1

    return hLine

  def get_amount_inside(self, shape):
    areaOutside = self.width * self.height
    areaInside = shape.width * shape.height

    canFit = areaOutside / areaInside
    return int(canFit)

  def __repr__(self):
      return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):

  def __init__(self, side):
    self.height = side
    self.width = side

  def set_side(self, newSide):
    self.width = newSide
    self.height = newSide

  def __repr__(self):
    return "Square(side=" + str(self.width) + ")"

