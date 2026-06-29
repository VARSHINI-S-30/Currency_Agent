import requests

def currency_converter(from_currency, to_currency, amount):
    """
    Convert currency using ExchangeRate API.

    from_currency : USD
    to_currency   : INR
    amount        : 100
    """

    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    response = requests.get(url)

    if response.status_code != 200:
        return "Unable to fetch exchange rates."

    data = response.json()

    if data["result"] != "success":
        return "Invalid currency."

    rates = data["rates"]

    if to_currency not in rates:
        return "Target currency not found."

    converted = amount * rates[to_currency]

    return (
        f"{amount} {from_currency} = "
        f"{converted:.2f} {to_currency}"
    )