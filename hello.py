# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from bs4 import BeautifulSoup
import requests

def scrape(input_url):
	r=requests.get(input_url)
	print (input_url)
	soup = BeautifulSoup(r.text, "html.parser")
	prod = soup.find('div', class_="_1vC4OE _37U4_g")
	prod_price = prod.text.replace(',', "").strip('₹')
	#prod_price = prod_price.text.replace('\n', "").strip()
	return prod_price

my_url = 'https://www.flipkart.com/samsung-6-2-kg-fully-automatic-top-load-washing-machine-grey/p/itmewa2xkfkeq9cz?pid=WMNEWA2XKFSHQZZG&srno=b_1_1&otracker=nmenu_sub_TVs%20and%20Appliances_0_Fully%20Automatic%20Top%20Load&lid=LSTWMNEWA2XKFSHQZZGDYJV2I&fm=organic&iid=947fc1ab-c348-42e9-b9dd-5b7cbe5da5d1.WMNEWA2XKFSHQZZG.SEARCH&ppt=Store%20Browse&ppn=Search%20Page&ssid=rzryb5yfcadg46ww1521612430562'

if __name__ == "__main__":
	print (scrape(my_url))
