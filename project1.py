from flask import Flask
from flask import request, redirect, url_for,render_template
from time import sleep
import sys
print sys.path
from hello import scrape

# libraries for automatic email sending
#import smtplib
#from string import Template
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText


#MY_ADDRESS = 'ankitsaurabh.iitkgp@gmail.com'
#PASSWORD = 'toolazy69'

app = Flask(__name__)

#reading text file as a template for e-mail
#def read_template(filename):
#	with open(filename, 'r', encoding='utf-8') as template_file:#opening text file to read
#        	template_file_content = template_file.read()
#	return Template(template_file_content)


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
			print scrape(product)
			return render_template('success.html')
		else:
			return render_template('success.html')

if __name__ == '__main__':
	app.run(debug = True)
