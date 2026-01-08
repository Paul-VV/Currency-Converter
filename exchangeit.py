"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Paul Vezhdel
Date:   August 01, 2025
"""

import currency

first_input = input('3-letter code for original currency: ')
second_input = input('3-letter code for the new currency: ')
amount = float(input('Amount of the original currency: '))
conversion = round(currency.exchange(first_input, second_input, amount), 3)
result = 'You can exchange ' + str(amount) + ' ' + first_input +         \
' for ' + str(conversion) + ' ' + second_input + '.'

print(result)
