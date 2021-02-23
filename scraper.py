from urllib.request import urlopen
from bs4 import BeautifulSoup

url_scrape="https://vinay-1210.web.app/"
request_page=urlopen(url_scrape)
page_html=request_page.read()
request_page.close()

html_soup= BeautifulSoup(page_html,'html.parser')

names=html_soup.find_all('div',class_="a")

filename='item.csv'
f=open(filename,'w')

headers='Names \n'

f.write(headers)

for name in names:
    n= name.find('h4',class_="name").text


    f.write(n)
f.close()