import time
import pandas as pd
import re
import pyarrow as pa
import pyarrow.parquet as pq
import numpy as np
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def parquet_file_write(data):
    value = pd.DataFrame(data)
    table = pa.Table.from_pandas(value)
    pq.write_table(table,"files/mobiles.parquet")

def variant_extract(data,mobile,price):
    pattern = r"[()]"
    match = re.search(pattern,mobile.get_attribute("innerHTML"))
    if match:
        list = re.split(pattern,mobile.get_attribute("innerHTML"))
        data.append({
            'Mobile':list[0],
            'Variant':list[1],
            'Price':price.get_attribute("innerHTML")
        })
    else:
        data.append({
            'Mobile':mobile.get_attribute("innerHTML"),
            'Price':price.get_attribute("innerHTML")
        })



def get_mobile_price(driver,data):
  
    time.sleep(20)
    mobiles = driver.find_elements("xpath","//div[@class='puisg-row']//h2//a//span")
    prices = driver.find_elements("xpath","//div[@class='puisg-row']//a//span[@class='a-price-whole']")   
    for mobile,price in zip(mobiles,prices):
        variant_extract(data,mobile,price)



def main():
    data = []
    options = Options()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
    search_bar = driver.find_element("xpath","/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
    search_bar.send_keys("Smartphones")
    search_button = driver.find_element("xpath","/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
    search_button.click()
    for page in range(1,5):
        get_mobile_price(driver,data)
        next_page = driver.find_element("xpath","//a[text()[contains(.,'Next')]]")
        time.sleep(20)
        next_page.click()        
    parquet_file_write(data)
    


if __name__ == '__main__':
    main()
    
   









