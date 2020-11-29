from pprint import pprint

"""

1. Представьте себе бухгалтерскую книгу в книжном магазине. В этой книге хранятся
записи о номере заказа, названии книги, колличестве и стоимости одной книги, как
представленно ниже, в таблице.
+--------------+------------------------------------+----------+----------------+
| Order Number | Book Title and Author | Quantity | Price per Item |
+--------------+------------------------------------+----------+----------------+
| 34587 | Learning Python, Mark Lutz | 4 | 40.95 |
| 98762 | Programming Python, Mark Lutz | 5 | 56.80 |
| 77226 | Head First Python, Paul Barry | 3 | 32.95 |
| 88112 | Einfuhrung in Python3, Bernd Klein | 3 | 24.99 |
+--------------+------------------------------------+----------+----------------+
Напишите программу на Python, которая на вход получает список списков:
[
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]
и возвращает список кортежей. Каждый кортеж состоит из номера заказа и произведения
цены на товары и количества. Стоимость товара должена быть увеличена на $10, если
стоимость заказа меньше $100. Программа должна использовать lambda и map

"""

ledger = [
    [34587, 'Learning Python, Mark Lutz', 4, 40.95],
    [98762, 'Programming Python, Mark Lutz', 5, 56.80],
    [77226, 'Head First Python, Paul Barry', 3, 32.95],
    [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]


# pprint(ledger)


# def func(a):
#     for order in a:
#         goods_sum = order[2] * order[3]
#         if goods_sum < 100:
#             goods_sum += 10
#         print(order[0], order[2] * order[3], '"', round(goods_sum, 2), '"')


res = tuple(map(lambda a: tuple(), ledger))
print(res)
# func(ledger)
# res = tuple()
# print(res, type(res), len(ledger), ledger[0][0])
