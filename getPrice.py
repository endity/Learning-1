import bs4 as bs
import urllib.request
import pandas as pd
import csv
import datetime as dt


def getPrice(site):
    """
    Function to get price from the site
    Return the lowest bottle price
    """

    source = urllib.request.urlopen(site).read()
    #source = urllib.request.urlopen('https://www.wine-searcher.com/find/conseillante/2016/france').read()

    # BEAUTIFULSOUP SCRAPPING
    soup = bs.BeautifulSoup(source, 'html5lib')
    title = soup.find('title').string
    title = title[:-26]
    table = soup.find('table', {'id': "wine_list"})
    div = soup.find('div', {'id': "winesortlist"})


    while True:
        try:
            rating = div.find('span', {'itemprop': "ratingValue"}).string
            break
        except:
            rating = "N/A"
            break

    table = soup.find('table', {'id': "wine_list"})


    #DECLARE EMPTY VARIABLE
    prices = []
    btlformats = []
    alist = []
    today = dt.datetime.today().strftime('%Y-%m-%d')
    # print(title)
    # type(table)
    # print(rating)

    for i in table.findAll('span', {'class':"offer_price"}):
        price = i.text.replace('\n', '')
        prices.append(price)

    if not prices:
        with open('winePrice.csv', 'a', newline='', encoding = 'utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([today, title, "Not Found", "N/A"])
        return None

    for j in table.findAll('span', {'class':"offer_btl"}):
        btlformat = j.text
        btlformats.append(btlformat)

    dictionary = dict(zip(prices, btlformats))

    for k, value in dictionary.items():
        if not value == 'Half Bottle' and value == 'Bottle':
            alist.append(k)

    with open('winePrice.csv', 'a', newline='', encoding = 'utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([today, title, str(alist), rating])



#getPrice('https://www.wine-searcher.com/find/forts+de+latour/2016/france')
# WRITE IN A NEW TXT FILE
# f = open("{}.txt".format(title.string), 'w+', encoding='utf-8')
# f.truncate()
# f.write(str(dictionary))
# f.close()

# WRITE IN THE CSV FILE
# df = pd.DataFrame(dictionary, index = [str(title.string)])
# df.to_csv('Wine_Price.csv')

# WRITE IN CSV VER2
# with open("Wine_Price.csv", "ab", newline = '') as g:
#     g.write(dictionary)
