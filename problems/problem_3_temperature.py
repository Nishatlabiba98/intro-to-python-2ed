"""
Convert a temperature from Fahrenheit to Celsius
"""
temp_f = input("Temp in °F: ")
temp_f = int (temp_f)
# Calculate it in Celsius
temp_c = (temp_f - 32) * 5/9
temp_c = str (temp_c)
print("Temp in °C: " + temp_c)
