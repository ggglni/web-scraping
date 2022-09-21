from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
    driver.get("https://ggglni.xyz/")
    return driver

def main():
    driver = get_driver()
    element = driver.find_element(by="xpath",value="/html/body/div[2]/p")
    return element, element.text

print(main())

