def parallel(resistor):
  
  total_resistance = 0
  
  for resistor_value in resistor:
    total_resistance += 1 / resistor_value

  final_resistance = 1 / total_resistance

  print(round(final_resistance, 3), "ohms") 

parallel([330, 1000, 2200])

def potential_divider( Input_Voltage,Resistors):
  
 R1, R2 = Resistors

 Output_Voltage1 = Input_Voltage * (R1/(R1 + R2))
 Output_Voltage2 = Input_Voltage * (R2/(R1 + R2))
  
 print(round (Output_Voltage1, 2), "v")
 print(round (Output_Voltage2, 2), "v")

potential_divider(9, [3000, 1000])
def temperature_check(temperature, unit ):
  
   hypothermia_C = 36.1
   hyperthermia_C = 37.5

   if unit == "F" :
     temperature = (temperature - 32) * 5/9

   if temperature < 36.1:
            print("the patient is hypothermic.")
   elif temperature > 37.5:
           print("the patient is hyperthermic .")
   else:
         print("The patient's temperature is normal.")
  

temperature_check(14, "C") 
temperature_check(37, "F")
temperature_check(37, "C")
