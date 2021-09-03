"""
ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.
"""
from decimal import Decimal

def decimal_list_generator():
    start_value = 2
    end_value = 5.5

    increment = 0.5
    int_list = []

    while start_value <= end_value:
        int_list.append(start_value)
        start_value += increment

    decimal_list = [Decimal(i) for i in int_list]
    return decimal_list

print(decimal_list_generator())
