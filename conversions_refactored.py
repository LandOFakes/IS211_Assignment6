class ConversionNotPossible(Exception):
    pass
def convert(fromUnit, toUnit, value):

if fromUnit == toUnit:
        return value

    temperature_conversions = {
        ('Celsius', 'Fahrenheit'): lambda x: (x * 9/5) + 32,
        ('Celsius', 'Kelvin'): lambda x: x + 273.15,
        ('Fahrenheit', 'Celsius'): lambda x: (x - 32) * 5/9,
        ('Fahrenheit', 'Kelvin'): lambda x: (x - 32) * 5/9 + 273.15,
        ('Kelvin', 'Celsius'): lambda x: x - 273.15,
        ('Kelvin', 'Fahrenheit'): lambda x: (x - 273.15) * 9/5 + 32,
    }

    distance_conversions = {
        ('Miles', 'Yards'): lambda x: x * 1760,
        ('Miles', 'Meters'): lambda x: x * 1609.34,
        ('Yards', 'Miles'): lambda x: x / 1760,
        ('Yards', 'Meters'): lambda x: x * 0.9144,
        ('Meters', 'Miles'): lambda x: x / 1609.34,
        ('Meters', 'Yards'): lambda x: x / 0.9144,
    }

    if (fromUnit, toUnit) in temperature_conversions:
        return temperature_conversions[(fromUnit, toUnit)](value)

    if (fromUnit, toUnit) in distance_conversions:
        return distance_conversions[(fromUnit, toUnit)](value)

    raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not possible.")
