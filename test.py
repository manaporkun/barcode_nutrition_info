import requests
from bs4 import BeautifulSoup


product = str(input('Please enter product name: ')).replace(' ', '+')

page = requests.get('https://www.fatsecret.com.tr/kaloriler-beslenme/search?q={}'.format(product))
soup = BeautifulSoup(page.text, 'html.parser')

nutrition_facts = soup.find(class_ = 'borderBottom')

artist_name_list_items = nutrition_facts.find_all('a')

link = artist_name_list_items[0].get('href')

page = requests.get('https://www.fatsecret.com.tr'+link)
soup = BeautifulSoup(page.text, 'html.parser')

manufacturer = soup.find(class_ = 'manufacturer').find_all('a')[0].string if soup.find(class_ = 'manufacturer') != None else ''
product_name = soup.find(class_ = 'center').find_all('h1')[0].string if soup.find(class_ = 'center') != None else ''

nutrition_facts = soup.find(class_ = 'generic spaced').find_all('div')

info = {
		'Manufacturer':manufacturer,
		'Name':product_name,
		nutrition_facts[0].string:nutrition_facts[1].string,
		nutrition_facts[2].string:nutrition_facts[3].string,
		nutrition_facts[4].string:nutrition_facts[5].string,
		nutrition_facts[6].string:nutrition_facts[7].string,
		}

print(info)