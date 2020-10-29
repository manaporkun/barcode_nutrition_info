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
	

def get_nutrition(product_url):

	soup = get_search_soup(product_name)

	product_page = requests.get(url+product_url)
	soup = BeautifulSoup(product_page.text, 'html.parser')

	nutrition_facts = soup.find(class_ = 'generic spaced').find_all('div') if soup.find(class_ = 'generic spaced') != None else []

	manufacturer = soup.find(class_ = 'manufacturer').find_all('a')[0].string if soup.find(class_ = 'manufacturer') != None else ''
	name = soup.find(class_ = 'center').find_all('h1')[0].string if soup.find(class_ = 'center') != None else ''
	calorie = nutrition_facts[1].string
	fat = nutrition_facts[3].string
	carbonhydrate = nutrition_facts[5].string
	protein = nutrition_facts[7].string

	info = {
			'Manufacturer':manufacturer,
			'Name':name,
			'Calorie':calorie,
			'Fat':fat,
			'Carbohydrate':carbonhydrate,
			'Protein':protein,
			}
	
	return info
