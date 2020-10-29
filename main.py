import product_info


product_name = str(input('Please enter product name: '))

try:
    product_list = product_info.get_product_list(product_name)
    for id, product in enumerate(product_list):
        print(id, product[2], product[3])

    selection = int(input('Please select one of the products: '))
    while selection >= len(product_list) & selection >= 0:
        selection = int(input('Please select again: '))

    selection_product_url = product_list[selection][0]
    selection_brand_url = product_list[selection][1]

    nutrition_info = product_info.get_nutrition(selection_product_url)
    for info in nutrition_info:
        print(info, nutrition_info[info])   

except:
    print('Product not found')