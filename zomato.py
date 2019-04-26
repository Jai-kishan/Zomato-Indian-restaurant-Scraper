#pprint — Data pretty printer. 
#The pprint module provides a capability to “pretty-print” arbitrary Python data structures in a form which can be used as input to the interpreter.
from pprint import pprint
#Selenium is a portable framework for testing web applications and ita a open source application.
#Selenium provides a playback tool for authoring functional tests without the need to learn a test scripting language
#Selenium WebDriver is a collection of open source APIs which are used to automate the testing of a web application.
from selenium import webdriver
# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
from bs4 import BeautifulSoup

home_url="https://www.zomato.com/dharamshala"

def request(url):
	driver = webdriver.Chrome()
	driver.get(url)
	response = driver.execute_script("return document.documentElement.outerHTML")
	soup = BeautifulSoup(response,'lxml')
	driver.quit()
	return soup

soup = request(home_url)
# pprint(soup)

collection_url = soup.find('div', class_='col-l-16 col-s-16').a.get('href')
response= request(collection_url)
restaurant_name = soup.find_all('div',class_="clearfix")
for i in restaurant_name:
	a=i.find('div',class_='heading bold ln20').get_text().strip()
	print(a)

# print(restaurant_name)






