import requests
from bs4 import BeautifulSoup

url = 'https://www.fatsecret.com.tr'
product_name = ''

def get_search_soup(product_name):
	product_name = product_name.replace(' ', '+')

	search_url = url + '/kaloriler-beslenme/search?q={}'.format(product_name)

	search_page = requests.get(search_url)
	soup = BeautifulSoup(search_page.text, 'html.parser')

	return soup


def get_product_list(product_name):
	
	soup = get_search_soup(product_name)

	product_list = []

	product = soup.find(class_ = 'generic searchResult')
	product_items = product.find_all('tr')
	
	for item in product_items:
		product_url = item.find(class_ = 'prominent').get('href')
		name = item.find(class_ = 'prominent').string
		brand = item.find(class_ = 'brand').string if item.find(class_ = 'brand') != None else ''
		brand_url = item.find(class_ = 'brand').get('href') if item.find(class_ = 'brand') != None else ''
		product_list.append([product_url, brand_url, name, brand])

	return product_list
	

def get_nutrition(product_url, product_info):

	soup = get_search_soup(product_name)

	product_page = requests.get(url+product_url)
	soup = BeautifulSoup(product_page.text, 'html.parser')

	soup_generic = soup.find(class_ = 'generic spaced')

	if soup_generic is not None:

		nutrition_facts = soup_generic.find_all('div')

		product_info['calorie'] = nutrition_facts[1].string
		product_info['fat'] = nutrition_facts[3].string
		product_info['carbonhydrate'] = nutrition_facts[5].string
		product_info['protein'] = nutrition_facts[7].string

	else:
		pass

	product_info['manufacturer'] = soup.find(class_ = 'manufacturer').find_all('a')[0].string if soup.find(class_ = 'manufacturer') != None else ''
	# name = soup.find(class_ = 'center').find_all('h1')[0].string if soup.find(class_ = 'center') != None else ''
	
	return product_info
