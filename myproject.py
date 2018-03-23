# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask
from flask import request, redirect, url_for,render_template
from bs4 import BeautifulSoup
import requests
from time import sleep

# libraries for automatic email sending
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


MY_ADDRESS = 'ankitsaurabh.iitkgp@gmail.com'
PASSWORD = 'toolazy69'

app = Flask(__name__)

#reading text file as a template for e-mail
def read_template(filename):
	with open(filename, 'r', encoding='utf-8') as template_file:#opening text file to read
        	template_file_content = template_file.read()
	return Template(template_file_content)

#scraping data using beautifulSoup
def scrape(input_url):
	r=requests.get(input_url)
	print (input_url)
	soup = BeautifulSoup(r.text, "html.parser")
	prod = soup.find('div', class_="_1vC4OE _37U4_g")#searched this class using Web develepor inspector
	prod_price = prod.text.replace(',', "").strip('₹')#removing the comma
	return prod_price


@app.route('/')
def yourscraper():
	return render_template('form.html')

#taking the url from action mentioned in form.html
@app.route('/flipkartScraper', methods = ['GET', 'POST'])
def final_page():
	if request.method=='POST' :
		user = request.form['mail']
		product = request.form['nm']
		my_price = request.form['price']
		
		if scrape(product)<my_price:
			#reading the template
			message = read_template('process.txt')
			message = message.substitute(PROD_P = scrape(product))
			#initiating the process for sending mail
			s = smtplib.SMTP(host='smtp-gmail.com', port=587)
			#encoding the mail
			s.starttls()
			s.login(MY_ADDRESS, PASSWORD)
			msg['From']=MY_ADDRESS
        		msg['To']=user
			msg['Subject']="ALERT"
			msg.attach(MIMEText(message, 'plain'))
			s.send_message(msg)
			#Terminate the SMTP session and close the connection
			s.quit()
			print scrape(product)
			return render_template('success.html')
		else:
			return render_template('success.html')

if __name__ == '__main__':
	app.run(debug = True)
