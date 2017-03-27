from concrete_resistance_n_deformation import *

class beton:

   name = ""
   fck = 0
   fck_cube = 0
   fcm = 0
   fatm = 0
   fck_005 = 0
   fck_095 = 0
   Ecm = 0

   def __init__(self, name):
      self.name = name
      self.fck = float(characteristic("fck",name))
      self.fck_cube = float(characteristic("fck_cube",name))
      self.fcm = float(characteristic("fcm",name))
      self.fatm = float(characteristic("fatm",name))
      self.fck_005 = float(characteristic("fck0.05",name))
      self.fck_095 = float(characteristic("fck0.95",name))
      self.Ecm = float(characteristic("Ecm",name))

   def stringify(self):
      as_string = ""
      as_string = as_string + self.name + " fck:" + str(self.fck)
      as_string = as_string + " fck_cube:" + str(self.fck_cube)
      as_string = as_string + " fcm:" + str(self.fcm)
      as_string = as_string + " fatm:" + str(self.fatm)
      as_string = as_string + " fck_0.05:" + str(self.fck_005)
      as_string = as_string + " fck_0.95:" + str(self.fck_095)
      as_string = as_string + " Ecm:" + str(self.Ecm)
      return as_string

