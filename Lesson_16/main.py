from Lesson_16.aval_parser import RaiffeisenBankAval
from Lesson_16.private_parser import PrivateBank
from Lesson_16.ukrsib_parser import UkrSibBank
from Lesson_16.obmenka_parser import ObmenkaPoint


banks = [
    RaiffeisenBankAval(),
    PrivateBank(),
    UkrSibBank(),
    ObmenkaPoint()
]

for bank in banks:
    rates = bank.get_currency_rate()['rate']
    for currency in rates:
        print(currency['currency'])
        print(currency['purchase_rate'])
        print(currency['sale_rate'])
        print('-' * 25)
    print()
    print()