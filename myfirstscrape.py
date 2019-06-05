from bs4 import BeautifulSoup
import urllib
from urllib import request
import os
import smtplib





page = urllib.request.urlopen('https://money.cnn.com/data/markets/')
soup = BeautifulSoup(page, features="html.parser")
soup.prettify()
class_gainers = soup.find('ul', {"class": "module-body wsod gainers"})
class_gainers_text = soup.find('ul', {"class": "module-body wsod gainers"}).get_text()
foo = class_gainers_text.strip().replace("\n\n\n\n\n\n\n", "\n").split("\n")
bar = [x for x in foo if x]
bar = bar[:-1]
barlist = []
counter = 0
skip = 3
end = len(bar)
for i in bar:
	barlist.append(bar[counter:skip])
	counter += 3
	skip += 3
	if counter >= end:
		break
for i in barlist:
	i[2] = float(i[2])
for i in barlist:
	if i[1][0] == "+":
		i[1] = float(i[1][1:-1])
	elif i[1][0] == "-":
		i[1] = float(i[1][1:-1])*-1
dictdef = [["Company Name: ", "Percent Change: ", "Somethin: "]for i in barlist]
dicter = list(map(dict, map(zip, dictdef, barlist)))
to_send = []
for i in dicter:
	for key, val in i.items():
		to_send.append(key + str(val))
		if key == 'Someshit: ':
			to_send.append('\n')
		
to_send = "\n".join(to_send) 

	
def send_mail():
	ADDRESS = "codecademytrials@gmail.com"
	TO  = "deanhisrael@yahoo.com"
	SUBJECT = "StockAdvice, here are some suggestions"
	message = "From: %s\r\n" % ADDRESS + "To: %s\r\n" % TO + "Subject: %s\r\n" % SUBJECT + "\r\n" + to_send
	GMAILACCOUNT = os.environ.get("GMAILUSER")
	GMAILPASSWORD = os.environ.get("GMAILPASSWORD")
	try:


		mailserver = smtplib.SMTP('smtp.gmail.com',587)
		# identify ourselves to smtp gmail client
		mailserver.ehlo()
		# secure our email with tls encryption
		mailserver.starttls()
		# re-identify ourselves as an encrypted connection
		mailserver.ehlo()
		mailserver.login(GMAILACCOUNT, GMAILPASSWORD)
		mailserver.sendmail(ADDRESS, TO, message)
		
		print ('ok the email was sent ')
	except:
		print ('can\'t send the Email')
	finally:
		mailserver.quit()

send_mail()
