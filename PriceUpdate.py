from WStest import *
import time
"""
Pull data from a list of websites

"""
wine_list = ['chasse spleen', 'sociando mallet', 'grand mayne', 'marquis de terme',\
            'talbot', 'giscours', 'feytit clinet', 'canon la gaffeliere', 'la conseillante']

year_list = ['2015', '2016']

html_list = []

for i in wine_list:
    i = i.replace(" ", "+")
    for j in year_list:
        html = "https://www.wine-searcher.com/find/" + i + "/" +\
            j + "/france"
        html_list.append(html)

for htmli in html_list:
    getPrice(htmli)
