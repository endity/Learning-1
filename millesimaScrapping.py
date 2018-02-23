import bs4 as bs
import urllib.request

#html = input('Please enter the Millesima website')
source = urllib.request.urlopen('https://fr.millesima.ch/chateau-sociando-mallet-2010.html').read()
soup = bs.BeautifulSoup(source, 'html5lib')

# Find Wine Name
title = soup.find('div', {'class': "top namePartPriceContainer"}).find('h1', {'class': "main_header"}).get_text()
description = soup.find('div', {'id': "product_longdescription_188156"}).get_text()
table = soup.find('table', {'class': "descriptiveAttributes"})
rows = table.findAll('tr')

# Write in txt file
f = open("MillesimaScraping.txt", 'a', encoding='utf-8')
f.write("\n" + title + "\n")
f.write(description + "\n")
f.write(rows + "\n")
f.close()


# table = soup.find('table', {'id': "wine_list"})
# div = soup.find('div', {'id': "winesortlist"})
