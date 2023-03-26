import math
import requests

# (x) Set-up
conversion_key = 'e4432fd140fc46cf93705436f38ad276'
conversion_url = f"https://openexchangerates.org/api/latest.json?app_id={conversion_key}"

# (1) Returns the volume of a sphere from the given radius
# sphere_volume(radius: number)
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# (2) Currency converter
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

    converted_amount = ((float(amount) / exchange_rates[from_currency.upper()]) * exchange_rates[to_currency])
    rounded_amount = round(converted_amount, 2)

    return rounded_amount



if __name__ == "__main__":
    print(convert_currency('USD', 'INR', 10))