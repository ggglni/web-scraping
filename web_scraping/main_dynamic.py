from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service("/Users/giorgiogiuliani/Desktop/Python/automate-everything/web_scraping/chromedriver")

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
    driver.get("https://automated.pythonanywhere.com/")
    return driver

def clean_text(text):
    """extract only temperature from text"""
    output = text.split(": ")
    return float(output[1])

def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

print(main())

