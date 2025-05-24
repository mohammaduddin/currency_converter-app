class Logger:
    def __init__(self):
        self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(message)


class CurrencyConverter:
    def __init__(self, rates):
        self.rates = rates
        self.logger = Logger()

    # this method is sent from main method with the values
    def convert(self, amount, from_currency, to_currency):
        
        # checks if currency rate is not available 
        if from_currency not in self.rates or to_currency not in self.rates[from_currency]:
            self.logger.log(f"conversion rate from {from_currency} to {to_currency} not available.")
            return None
        
        # if currency rate is available then compute rate and then convert
        rate = self.rates[from_currency][to_currency]
        converted_amount = amount * rate
        self.logger.log(f"converted {amount} {from_currency} to {converted_amount:.2f} {to_currency} at rate {rate}.")
        return converted_amount


# main method
if __name__ == "__main__":
    # manually estimated exchange rates (such as, EUR/USD, GBP/JPY, EUR/AED, USD/CAD, USD/JPY)
    # stores currency rate in a dictionary
    exchange_rates = {
        "GBP": {"USD": 1.14, "EUR": 1.19, "JPY": 1.62},
        "EUR": {"USD": 0.95, "AUD": 1.47, "AED": 3.51},
        "USD": {"CAD": 1.15, "EUR": 0.74, "JPY": 120.7},
    }

    # passing exchange rates into "converter" variable
    converter = CurrencyConverter(exchange_rates)

    # convert to supported currency
    converter.convert(100, "USD", "CAD")
    converter.convert(200, "EUR", "AUD")
    converter.convert(500, "GBP", "JPY")

    # convert to unsupported currency
    converter.convert(50, "USD", "BDT")
    converter.convert(50, "CHF", "USD")


# OUTPUT:
# converted 100 USD to 115.00 CAD at rate 1.15.
# converted 200 EUR to 294.00 AUD at rate 1.47.
# converted 500 GBP to 810.00 JPY at rate 1.62.
# conversion rate from USD to BDT not available.
# conversion rate from CHF to USD not available.
