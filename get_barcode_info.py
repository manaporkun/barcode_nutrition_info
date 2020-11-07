import requests
from bs4 import BeautifulSoup
from product_info import get_nutrition

url = 'http://m.barkodoku.com/'


def get_barcode(barcode):

	barcode_page = requests.get(url + barcode)
	soup = BeautifulSoup(barcode_page.text, 'html.parser')

	my_soup = soup.find("span", {"id": "lblSonuclar"})

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

	if my_soup is not None:
		barcode_info['name'] = my_soup.find_all('a')[0].string
		barcode_info['manufacturer'] = my_soup.find_all('br')[2].string
		barcode_info['country'] = my_soup.find_all('br')[1].string
		barcode_info['price'] = my_soup.find_all('br')[4].string
	else:
		pass

	barcode_info = get_nutrition(barcode_info)
	
	return barcode_info