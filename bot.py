import requests
import bs4
from selenium import webdriver
from config import keys
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == '__main__':
    # Initiate the browser
    browser  = webdriver.Chrome(ChromeDriverManager().install())

    jackets = 'jackets'
    tops = 'tops_sweaters'
    product = 'Toshio Saeki'
    color = 'Navy'

    baseUrl = "https://www.supremenewyork.com/"
    shop = "shop/all/"
    checkout = "checkout/"

    r = requests.get("{}{}{}".format(baseUrl, shop, jackets)).text

    soup = bs4.BeautifulSoup(r, 'lxml')

    tempTuple = []
    tempLink = []

    for link in soup.find_all('a', href=True):
        tempTuple.append((link['href'], link.text))
    for i in tempTuple:
        if i[1] == product or i[1] == color:
            tempLink.append(i[0])

    print(tempLink)
    # Open the Website
    browser.get('{}{}'.format(baseUrl, tempLink[0]))