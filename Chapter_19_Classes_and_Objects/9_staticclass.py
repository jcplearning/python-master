#Create a class TemperatureConverter with static methods:
#celsius_to_fahrenheit(celsius) and fahrenheit_to_celsius(fahrenheit).

class Temperature:
    #@staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    #@staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
# Example usage:
print(Temperature.celsius_to_fahrenheit(25))  # Output: 77.0
print(Temperature.fahrenheit_to_celsius(77))  # Output: 25.0

