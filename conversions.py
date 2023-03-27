import math
import requests

# Credits:
# Currency conversion: https://openexchangerates.org/
# Conversion API documentation: https://docs.openexchangerates.org/reference/api-introduction
# Requests API documentation: https://requests.readthedocs.io/en/latest/

# (x) Set-up
conversion_key = 'e4432fd140fc46cf93705436f38ad276'
conversion_url = f"https://openexchangerates.org/api/latest.json?app_id={conversion_key}"

# (1) Returns the volume of a sphere from the given radius
# sphere_volume(radius: number)
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# (2) Area of a trapezoid from the given base lengths and height
# trapezoid_area(base_a, base_b, height)
def trapezoid_area(base_a, base_b, height):
    return (base_a + base_b) * height / 2

# (3) Currency converter
# currency_code: ISO 4217 compliant code for currency
# convert_currency(from_currency: currency_code, to_currency: currency_code, amount: number)
def convert_currency(from_currency, to_currency, amount):

    # Update the current rates (from openexchangerates.org)
    conversion_response = requests.get(conversion_url)
    conversion_data = conversion_response.json()
    exchange_rates = conversion_data["rates"]

    # Calculate the original and converted amounts and return it.
    # The openexchangerates API compares the currency rate to USD, so you have to do some math to find out the conversion rate.
    # [ It divides the original amount by "from_currency" to get the rate in USD (the "base rate") then multiplies it by the
    # "to_currency" exchange rate. ]

    converted_amount = ((float(amount) / exchange_rates[from_currency.upper()]) * exchange_rates[to_currency.upper()])
    rounded_amount = round(converted_amount, 2)

    return rounded_amount

# Main code to handle inputs and descriptions
if __name__ == "__main__":

    # Input handling for sphere volume
    print('This program will take you through 3 conversion calculators. It requires internet connection.')
    print("""
        1: Volume of a sphere
        Description: The calculator finds the volume of a sphere from the given inputs.
        Function usage: sphere_volume(radius: number)
        Returns: (volume: number)
    """)
    radius_input = float(input('What is the radius of the sphere?: '))
    print(f"The volume of the sphere is {sphere_volume(radius_input)}")

    # Input handling for trapezoid area
    print("""
        2: Trapezoid area
        Description: The calculator finds the area of a trapezoid from the given inputs.
        Function usage: trapezoid_area(base_a, base_b, height)
        Returns: (area: number)
    """)
    base_a_input = float(input('Length of base A: '))
    base_b_input = float(input('Length of base B: '))
    height_input = float(input('Height of the trapezoid: '))
    print(f"The area of the trapezoid is: {trapezoid_area(base_a_input, base_b_input, height_input)}")

    print("""
        3: Currency conversions
        Description: The calculator converts currency between different standards and amounts. It fetches the values
        live from openexchangerates.org. Use ISO Standard currency codes.
        Function usage: convert_currency(from_currency, to_currency, amount)
        Returns: (amount_in_converted_currency: number)
    """)

    # Input handling for currency
    from_currency_input = str(input('What currency are you converting from? (i.e. USD): '))
    to_currency_input = str(input("What currency are you converting to?: "))
    amount_input = float(input('What is the amount of the original currency?: '))
    print('Thinking...')
    print(f"{amount_input} {from_currency_input} is {convert_currency(from_currency_input, to_currency_input, amount_input)} {to_currency_input}")