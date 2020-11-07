import requests
from bs4 import BeautifulSoup

url = 'http://m.barkodoku.com/'


def get_product(barcode):

	barcode_page = requests.get(url + barcode)
	soup = BeautifulSoup(barcode_page.text, 'html.parser')

	my_soup = soup.find("span", {"id": "lblSonuclar"})

	barcode_info = {
		'manufacturer': '',
		'name': '',
		'barcode': barcode,
		'country': '',
		'code': '',
		'price': '',
		'date': '',
		'area:': ''
	}
	if my_soup is not None:
		barcode_info['name'] = my_soup.find_all('a')[0].string
	else:
		pass
	
	return barcode_info
	

	"""
	if soup.find(id_='lblSonuclar') is not None:
		name = soup.find(id_='lblSonuclar').find_all('a')[0].string
		barcode_code = soup.find(id_='lblSonuclar').find_all('br')[0].string
		country = soup.find(id_='lblSonuclar').find_all('br')[1].string
		manufacturer_code = soup.find(id_='lblSonuclar').find_all('br')[2].string
		product_code = soup.find(id_='lblSonuclar').find_all('br')[3].string
		price = soup.find(id_='lblSonuclar').find_all('br')[4].string
		price_date = soup.find(id_='lblSonuclar').find_all('br')[5].string
		price_area = soup.find(id_='lblSonuclar').find_all('br')[6].string

	else:
		name = ''
		barcode_code = ''
		country = ''
		manufacturer_code = ''
		product_code = ''
		price = ''
		price_date = ''
		price_area = ''

	info = {
		'manufacturer': manufacturer_code,
		'name': name,
		'barcode': barcode_code,
		'country': country,
		'code': product_code,
		'price': price,
		'date': price_date,
		'area:': price_area
	}

	return info
	"""