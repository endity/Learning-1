import bs4 as bs
import urllib.request

wssite = input("Enter the wine-searcher website")
source = urllib.request.urlopen(str(wssite)).read()
soup = bs.BeautifulSoup(source, 'html5lib')

title = soup.find('title')
table = soup.find('table', {'id': "wine_list"})
prices = []
btlformats = []

for i in table.findAll('span', {'class':"offer_price"}):
    price = i.text.replace('\n', '')
    prices.append(price)
for j in table.findAll('span', {'class':"offer_btl"}):
    btlformat = j.text
    btlformats.append(btlformat)

dictionary = dict(zip(prices, btlformats))

f = open("{}.txt".format(title.string), 'w+', encoding='utf-8')
f.truncate()
f.write(str(dictionary))

f.close()
