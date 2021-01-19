
#Description: Get the current price of crypto currencies

#Import the request libraries
from bs4 import BeautifulSoup
import requests
import time

#Create a function to get the price of a cryptocurrency
def get_crypto_price(coin):
    #Get the URL for example
    url = "https://www.google.com/search?client=firefox-b-d&q="+coin+"+priceX"

    #Make a request to the website
    HTML = requests.get(url)

    #Parse to HTML
    soup = BeautifulSoup(HTML.text, "html.parser")
    #Find the current price
    text = soup.find("div", attrs={"class":"BNeawe iBp4i AP7Wnd"}).find("div", attrs={"class":"BNeawe iBp4i AP7Wnd"}).text

    #Return the text
    return text

#Ger the price of a cryptocurrency
price = get_crypto_price("bitcoin")

#Create a function to consistently show the price of the cryptocurrency when it changes
def main():
    last_price = -1
    #create a loop to continuously show the price
    while True:
            #Choose the cryptocurrency that i want to get the price for
            crypto = "Bitcoin"
            #Get the price of the cryptocurrency
            price = get_crypto_price(crypto)
            #Check if the price changed
            if price != last_price:
                print(crypto+" price: ", price)
                last_price = price
            time.sleep(3)

#Run/execute the main function
main()