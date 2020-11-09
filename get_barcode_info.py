import requests
from bs4 import BeautifulSoup
from product_info import get_nutrition, get_product_list

url = 'http://barkodoku.com/'


def get_barcode_information(barcode):

	barcode_page = requests.get(url + barcode)
	soup = BeautifulSoup(barcode_page.text, 'html.parser')

	my_soup = soup.find("div", {"class": "col-xs-24 col-sm-24 col-md-9 excerpet"})

	barcode_info = {
		'manufacturer': '',
		'name': '',
		'barcode': barcode,
		'country': '',
		'price': '',
		'calorie': '',
		'fat': '',
		'carbonhydrate:': '',
		'protein':''
	}
	try:
		if my_soup is not None:
			barcode_info['name'] = my_soup.find_all('a')[0].string
			barcode_info['date'] = my_soup.find_all('span')[1].string
			barcode_info['country'] = my_soup.find_all('span')[3].string
			barcode_info['price'] = my_soup.find_all('span')[2].string
		else:
			return 
		
		product_name = barcode_info['name']
		product_list = get_product_list(product_name)
		barcode_info = get_nutrition(product_list[0][0], barcode_info)
	except IndexError:
		print('\n'+barcode+'\n')
	
	return barcode_info
	