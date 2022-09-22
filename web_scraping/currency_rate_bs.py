from bs4 import BeautifulSoup
import requests 

def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=100000.0'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    #find() returns the tag
    #get_text() returns only the tag content
    rate = (rate[0:-11]) 
    print(rate)
    value = int(rate)
    #get the text without the last 4 characters and convert it into a float    
    return value

get_currency('eur','try')