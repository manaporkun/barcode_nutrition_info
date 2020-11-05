import requests
from bs4 import BeautifulSoup

url = 'http://m.barkodoku.com/'


def get_search_soup(barcode):

	search_url = url + barcode

	search_page = requests.get(search_url)
	soup = BeautifulSoup(search_page.text, 'html.parser')

	return soup


def get_product(product_url, barcode):

	soup = get_search_soup(barcode)

	product_page = requests.get(url+product_url)
	soup = BeautifulSoup(product_page.text, 'html.parser')

    a = soup.find(id_ = 'lblSonuclar')
        
	name = a.find_all('a')[0].string if soup.find(id_ = 'lblSonuclar') != None else ''
	barcode_code = a.find_all('br')[0].string if soup.find(id_ = 'lblSonuclar') != None else ''
	country = a.find_all('br')[1].string if soup.find(id_ = 'lblSonuclar') != None else ''
	manufacturer_code = soup.find(id_ = 'lblSonuclar').find_all('br')[2].string if soup.find(id_ = 'lblSonuclar') != None else ''
    product_code = a.find_all('br')[3].string if soup.find(id_ = 'lblSonuclar') != None else ''
    price = a.find_all('br')[4].string if soup.find(id_ = 'lblSonuclar') != None else ''
    price_date = soup.find(id_ = 'lblSonuclar').find_all('br')[5].string if soup.find(id_ = 'lblSonuclar') != None else ''
    price_area = soup.find(id_ = 'lblSonuclar').find_all('br')[6].string if soup.find(id_ = 'lblSonuclar') != None else ''

	info = {
			'Manufacturer Code:':manufacturer_code,
			'Name:':name,
			'Barcode:':barcode_code,
			'Country':country,
			'Product Code':product_code,
			'Price:':price,
            'Price Date:':price_date,
            'Price Area:':price_area
			}
	
	return info
