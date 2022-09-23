#from bs4 import BeautifulSoup
#import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service("/Users/giorgiogiuliani/Desktop/Python/automate-everything/2_stock_notifier/chromedriver")

#with BS
# def get_delta():
#     url = f'https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6'
#     content = requests.get(url).text
#     soup = BeautifulSoup(content, 'html.parser')
#     delta = soup.find('span',class_='stock-value').get_text()
#     print(delta)

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
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver

def get_delta():
    driver = get_driver()
    time.sleep(2)
    driver.find_element(by="xpath",value="/html/body/div[1]/div/section[1]/div/div/div[2]/span")
    
    

# def send_notifications():
#     return

def main():    
    get_delta()
    #send_notifications() 
    
main()