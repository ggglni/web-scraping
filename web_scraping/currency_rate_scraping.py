from  bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("/Users/giorgiogiuliani/Desktop/Python/automate-everything/web_scraping/chromedriver")

#URL creation
amount = float(input('How much do you want to change?'))
input_currency = str(input('From which currency?'))
output_currency = str(input('Into which currency?'))
url = f'https://www.x-rates.com/calculator/?from={input_currency}&to={output_currency}&amount={amount}'
headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
content = str(requests.get(url, headers=headers).content)


def get_driver():
    #set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    
    #driver created
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    return driver

def main():
    driver = get_driver()
    change = driver.find_element(by="xpath",value="/html/body/div[2]/div/div[3]/div[1]/div/div[1]/div/div/span[2]")
    
    print(f'{amount} {input_currency} is equal to {change.text}')
    
main()