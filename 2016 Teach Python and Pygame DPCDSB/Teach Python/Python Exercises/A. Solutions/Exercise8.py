""" Solution to exercise 8 from the Chapter 2 extra notes
Sam Scott, 2016"""

# INPUT PHASE
tc = float(input("Enter the temperature in Celcius: "))
vk = float(input("Enter the wind speed in km/h: "))

# PROCESSING PHASE

# 1. convert temp to Fahrenheit and speed to m/h
tf = 9/5*tc + 32
vm = vk * 5 / 8

# 2. get the new temperature
twcf = 35.74 + 0.6215 * tf - 35.75 * vm**0.16 + 0.4275 * tf * vm**0.16

# 3. convert back to celcius
twcc = (twcf-32) * 5 / 9

# OUTPUT PHASE
print("The temperature with wind chill is",twcc,"degrees Celsius")