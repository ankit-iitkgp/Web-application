# Web-application
Making a web application to alert the user when the price of his desired product is within his range.
Although, it  is a single-time run.To use it you have to install flask, BeautifulScoup and smtplib.

To run the code, Save all the .html file in a folder named templates since they are returned through render_template.
Also, run project1.py to make the web application working without sending e-mail. Run myproject.py to send the e-mail too.

WORKING-
First of all it is parsing through web page of the url provided. In that it scraping the price.The scraping function returned the price.
Next, through Flask, it is making a web form in which you have to enter your e-mail id, url of the product and your desired price.
After that through simple if-else statements, it compare the returned price with your entered price suitably load a webpage nad send mail.
