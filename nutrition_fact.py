import requests
from bs4 import BeautifulSoup


product = str(input('Please enter product name: ')).replace(' ', '+')

url = 'https://www.fatsecret.com.tr'
search_url = url + '/kaloriler-beslenme/search?q={}'.format(product)

search_page = requests.get(search_url)
soup = BeautifulSoup(search_page.text, 'html.parser')

nutrition_facts = soup.find(class_ = 'borderBottom')
fact_items = nutrition_facts.find_all('a')
product_url = fact_items[0].get('href')

product_page = requests.get(url+product_url)
soup = BeautifulSoup(product_page.text, 'html.parser')

nutrition_facts = soup.find(class_ = 'generic spaced').find_all('div') if soup.find(class_ = 'generic spaced') != None else []

manufacturer = soup.find(class_ = 'manufacturer').find_all('a')[0].string if soup.find(class_ = 'manufacturer') != None else ''
product_name = soup.find(class_ = 'center').find_all('h1')[0].string if soup.find(class_ = 'center') != None else ''
calorie = nutrition_facts[1].string
fat = nutrition_facts[3].string
carbonhydrate = nutrition_facts[5].string
protein = nutrition_facts[7].string

info = {
		'Manufacturer':manufacturer,
		'Name':product_name,
		'Calorie':calorie,
		'Fat':fat,
		'Carbohydrate':carbonhydrate,
		'Protein':protein,
		}

print(info)