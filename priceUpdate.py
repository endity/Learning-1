from getPrice import *
from getPriceList2 import WineReference, WineYear
import time
"""
Pull data from a list of websites

"""
# wine_list = ['chasse spleen', 'sociando mallet', 'grand mayne', 'marquis de terme',\
#             'talbot', 'giscours', 'feytit clinet', 'canon la gaffeliere', 'la conseillante']
#
html_list = []

for (i, j) in zip(WineReference, WineYear):
    i = i.replace(" ", "+")
    html = "https://www.wine-searcher.com/find/" + i + "/" +\
        str(j) + "/france"
    html_list.append(html)

for htmli in html_list:
    getPrice(htmli)
