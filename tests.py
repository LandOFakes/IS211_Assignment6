import unittest
from conversions_refactored import convert, ConversionNotPossible

class TestConversions(unittest.TestCase):

    # Temperature Conversion
    def test_celsius_to_kelvin(self):
        self.assertEqual(convert('Celsius', 'Kelvin', 0), 273.15)
    
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(convert('Celsius', 'Fahrenheit', 0), 32)
    
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(convert('Fahrenheit', 'Celsius', 32), 0)
    
    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(convert('Fahrenheit', 'Kelvin', 32), 273.15)
    
    def test_kelvin_to_celsius(self):
        self.assertEqual(convert('Kelvin', 'Celsius', 273.15), 0)
    
    def test_kelvin_to_fahrenheit(self):
        self.assertEqual(convert('Kelvin', 'Fahrenheit', 273.15), 32)

    # Distance Conversion Tests
    def test_miles_to_yards(self):
        self.assertEqual(convert('Miles', 'Yards', 1), 1760)

    def test_miles_to_meters(self):
        self.assertEqual(convert('Miles', 'Meters', 1), 1609.34)

    def test_yards_to_miles(self):
        self.assertEqual(convert('Yards', 'Miles', 1760), 1)

    def test_yards_to_meters(self):
        self.assertEqual(convert('Yards', 'Meters', 1), 0.9144)

    def test_meters_to_miles(self):
        self.assertEqual(convert('Meters', 'Miles', 1609.34), 1)

    def test_meters_to_yards(self):
        self.assertAlmostEqual(convert('Meters', 'Yards', 1), 1.09361, places=5)

    # Identity Conversion
    def test_identity_conversion(self):
        self.assertEqual(convert('Celsius', 'Celsius', 100), 100)
        self.assertEqual(convert('Fahrenheit', 'Fahrenheit', 100), 100)
        self.assertEqual(convert('Kelvin', 'Kelvin', 100), 100)
        self.assertEqual(convert('Miles', 'Miles', 100), 100)
        self.assertEqual(convert('Yards', 'Yards', 100), 100)
        self.assertEqual(convert('Meters', 'Meters', 100), 100)

    # Invalid Conversion 
    def test_invalid_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            convert('Celsius', 'Miles', 100)
        
        with self.assertRaises(ConversionNotPossible):
            convert('Kelvin', 'Yards', 100)
        
        with self.assertRaises(ConversionNotPossible):
            convert('Fahrenheit', 'Meters', 100)

if __name__ == '__main__':
    unittest.main()
