def parallel(resistor):
  
  total_resistance = 0
  
  for resistor_value in resistor:
    total_resistance += 1 / resistor_value

  final_resistance = 1 / total_resistance

  print(round(final_resistance, 3), "ohms") 

parallel([330, 1000, 2200])