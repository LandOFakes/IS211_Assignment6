class ConversionNotPossible(Exception):
     pass

def convert(fromUnit, toUnit, value):
     
     if fromUnit == toUnit:
          return value

    # Temperature Conversions
          if fromUnit == 'Celsius' and toUnit == 'Kelvin':
             return value + 273.15
          elif fromUnit == 'Celsius' and toUnit == 'Fahrenheit':
             return (value * 9/5) + 32
          elif fromUnit == 'Fahrenheit' and toUnit == 'Celsius':
             return (value - 32) * 5/9
          elif fromUnit == 'Fahrenheit' and toUnit == 'Kelvin':
             return (value - 32) * 5/9 + 273.15
          elif fromUnit == 'Kelvin' and toUnit == 'Celsius':
             return value - 273.15
          elif fromUnit == 'Kelvin' and toUnit == 'Fahrenheit':
             return (value - 273.15) * 9/5 + 32

    # Distance Conversions
          elif fromUnit == 'Miles' and toUnit == 'Yards':
               return value * 1760
          elif fromUnit == 'Miles' and toUnit == 'Meters':
               return value * 1609.34
          elif fromUnit == 'Yards' and toUnit == 'Miles':
               return value / 1760
          elif fromUnit == 'Yards' and toUnit == 'Meters':
               return value * 0.9144
          elif fromUnit == 'Meters' and toUnit == 'Miles':
               return value / 1609.34
          elif fromUnit == 'Meters' and toUnit == 'Yards':
               return value * 1.09361

 # conversion not supported
raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit}")
