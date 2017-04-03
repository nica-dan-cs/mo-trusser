
class otel:

   european_name = ""
   comercial_name = ""
   minimum_diameter = 0
   maximum_diameter = 0
   fyk = 0
   ft = 0

   def __init__(self, otel_df):
      self.european_name = otel_df['european_name']
      self.comercial_name = otel_df['comercial_name']
      self.minimum_diameter = float(otel_df['minimum_diameter'])
      self.maximum_diameter = float(otel_df['maximum_diameter'])
      self.fyk = float(otel_df['fyk'])
      self.ft = float(otel_df['ft'])

   def retrieve_name(self):
      return self.european_name + " / " + self.comercial_name
