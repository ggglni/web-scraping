from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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
    driver.get("https://www.coursera.org/login")
    return driver

def clean_text(text):
    """extract only temperature from text"""
    output = text.split(": ")
    return float(output[1])

def main():
    driver = get_driver()
    driver.find_element(by="id",value="email").send_keys("giorgio.giulianifiacco@gmail.com") #username entered
    time.sleep(2)
    driver.find_element(by='id', value='password').send_keys('Sergio!86' + Keys.RETURN) #password entered
    time.sleep(2)
    driver.find_element(by='xpath', value='/html/body/div[2]/div/div/div/div/div/section/section/div[1]/form/button').click()
    print(driver.current_url)
    
    
main()

