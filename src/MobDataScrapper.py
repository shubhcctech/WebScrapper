import time
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import numpy as np
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




def get_mobile_price(page):
    time.sleep(20)
    mobiles = driver.find_elements("xpath","//div[@class='puisg-row']//h2//a//span")
    prices = driver.find_elements("xpath","//div[@class='puisg-row']//a//span[@class='a-price-whole']")   
    for mobile,price in zip(mobiles,prices):
        value = pd.DataFrame({'Mobile':[mobile.get_attribute("innerHTML")],
                              'Price':[price.get_attribute("innerHTML")]},
                              index= list('123'))
        table = pa.Table.from_pandas(value)
        pq.write_table(table,f'files/mobiles{page}.parquet')
        # file.write(mobile.get_attribute("innerHTML"))
        # file.write("\n")
        # file.write(f"Price:{price.get_attribute("innerHTML")}")
        # file.write("\n\n")
    file.close()
    


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
    get_mobile_price(page)
    next_page = driver.find_element("xpath","//a[text()[contains(.,'Next')]]")
    time.sleep(20)
    next_page.click()                       
    
   








