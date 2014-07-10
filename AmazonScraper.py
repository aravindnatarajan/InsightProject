import urllib
import urllib2
import string
import sys
from bs4 import BeautifulSoup
import sqlite3
from datetime import date
from time import sleep
import sys
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('product', metavar='product', type=str, nargs=1,
                   help='URL of product')
parser.add_argument('target', metavar='target',type=float , nargs=1,
                   help='target price')

args = parser.parse_args()

product = args.product[0]
target = args.target[0]
csvfile = r'c:\users\owner\documents\python\amazon.csv'

def send_text(message):    
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:13.0) Gecko/20100101 Firefox/13.0'
    headers = { 'User-Agent' : user_agent }

    url = "http://somephpfile.php"
    values = {"to":"********",
              "from":"********",
              "sub":"Amazon Price Alert",
              "msg":message,
              "pwd":"******"}

    data = urllib.urlencode(values)
    print data
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()    

    print the_page


user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:13.0) Gecko/20100101 Firefox/13.0'
headers = { 'User-Agent' : user_agent }
request=urllib2.Request(product,None ,headers)
response = urllib2.urlopen(request)
the_page = response.read()

soup= BeautifulSoup(the_page)


title = soup.find("span",{"id":"btAsinTitle"})
con = title.contents

title = con[0]
if len(title)>50:
    title = title[0:50]+"..."

price = unicode(soup.find("b",{"class":"priceLarge"}).string).strip()


#get rid of dollar sign
price_dec = float(price[1:])


today = date.today().strftime("%x")
f= open(csvfile,"a")
f.write("\""+today+"\",\""+title+"\",\""+price+"\"\n")
f.close()

if price_dec <= target:
    print title +" "+ price + " Matched price!"
    message =  title + " is on sale for " + price + "\n "+product
    send_text(message)

else:
    print title +" "+ price + " Does not meet target price"


