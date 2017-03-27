class metal:

   european_name = ""
   comercial_name = ""
   minimum_diameter = 0
   maximum_diameter = 0
   fyk = 0
   ft = 0

   def __init__(self, metal_df):
      self.european_name = metal_df['european_name']
      self.comercial_name = metal_df['comercial_name']
      self.minimum_diameter = float(metal_df['minimum_diameter'])
      self.maximum_diameter = float(metal_df['maximum_diameter'])
      self.fyk = float(metal_df['fyk'])
      self.ft = float(metal_df['ft'])