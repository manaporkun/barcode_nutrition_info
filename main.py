from os import error
import product_info
from barcode_scanner import read_barcode
from get_barcode_info import read_barcode
from database_operations import mongoDB


db = mongoDB('product', 'barcode')
#query = {'barcode':'8699809190139'}
#print(db.get(query)[0])
read_barcode(db)

"""
# product = get_product('8695077102010')
db = mongoDB('product', 'barcode')

query = {'barcode':'8695077102010'}
# column = db.push(product)
print(db.get(query)[0])

"""

"""
try:

    db = mongoDB()

    if not db.if_exists_db('product') and not db.if_exists_table('barcode'):
        db.create('product', 'barcode')
        column = db.push(product)
        print(column)


except:
    print('error')
"""

# get_barcode()
# print(get_product('8695077102010'))

"""
product_name = str(input('Please enter product name: '))

try:
    product_list = product_info.get_product_list(product_name)
    for id, product in enumerate(product_list):
        print(id, product[2], product[3])

    selection = int(input('Please select one of the products: '))
    while selection >= len(product_list) & selection < 0:
        selection = int(input('Please select again: '))

    selection_product_url = product_list[selection][0]
    selection_brand_url = product_list[selection][1]

    nutrition_info = product_info.get_nutrition(selection_product_url)
    for info in nutrition_info:
        print(info, ':', nutrition_info[info])   

except:
    print('Product not found')

"""