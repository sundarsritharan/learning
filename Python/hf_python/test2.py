product = { 'Book' : 49.99,
            'PDF' : 43.99,
            'Video': 199.99
 }

for k in product:
    print(k, '->', product[k])

print('----')

for k in sorted(product, key=product.get):
    print(k, '->', product[k])

print('----')

for k in sorted(product, key=product.get, reverse=True):
    print(k, '->', product[k])