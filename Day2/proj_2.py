celsius_str: int = input('Enter value: ')
celsius = float(celsius_str)
CONSTANT: float = 273.15
kelvin = celsius + CONSTANT
print(f'{celsius} celsius to kevlin is {kelvin}')