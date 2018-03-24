# coding: utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Flask
from flask import request, redirect, url_for,render_template
from bs4 import BeautifulSoup
import requests
from time import sleep

from flask_mail import Mail, Message

app = Flask(__name__)

#using flask mail
#setting all the configurations.
mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ankitsaurabh.iitkgp@gmail.com'
app.config['MAIL_PASSWORD'] = 'toolazy69'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

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

@app.route('/sendMail<username>')
def index(username):
	#defining the e-mail.
	msg = Message('Alert',sender = 'ankitsaurabh.iitkgp@gmail.com', recipients = [username])
  	msg.body = "Hurry up! your product is within your range"
   	mail.send(msg)
	return render_template('success.html')


#taking the url from action mentioned in form.html
@app.route('/flipkartScraper', methods = ['POST','GET'])
def final_page():
	if request.method=='POST' :
		user = request.form['mail']
		product = request.form['nm']
		my_price = request.form['price']
		print scrape(product)
		
		if scrape(product)<my_price:
			#starting the process of sending mail.Since the condition is satisfied.
			return redirect(url_for('index', username=user))
		else:
			return render_template('failure.html')



if __name__ == '__main__':
	app.run(debug = True)
