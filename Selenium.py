from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
from random import randint

def driver(path, headless=True):
    options = Options()
    options.headless = headless
    driver_service = Service(executable_path=path)
    driver = webdriver.Chrome(service=driver_service, options=options)
    return driver

def get_quotes(driver,page=1):
    link = f"http://quotes.toscrape.com/page/{page}"
    driver.get(link)
    containers = driver.find_elements(by='xpath', value="//div[@class='quote']")
    scrape = {'page':page,'quotes': [], 'authors': []}
    for container in containers:
        scrape['quotes'].append(container.find_element(by='xpath', value="./span[@class='text']").text)
        scrape['authors'].append(container.find_element(by='xpath', value="./span/small[@class='author']").text)
    driver.quit()
    return scrape

def csv(dictQuotes):
    date = datetime.now().strftime("%Y%m")
    csv = f"quotes_page-{dictQuotes['page']}_{date}.csv"
    del dictQuotes['page']
    df = pd.DataFrame(dictQuotes)
    df.to_csv(f'./{csv}')

driver = driver(input("driver path: "))
scrape = get_quotes(driver,page=randint(1,10))
csv(scrape)
