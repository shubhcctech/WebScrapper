from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

file = open("files/mobiles.txt",'w')
options = Options()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)

driver.get("https://www.amazon.in/")
driver.maximize_window()
search_bar = driver.find_element("xpath","//div[@class = 'nav-search-field ']/input[@id='twotabsearchtextbox']")
search_bar.send_keys("Smartphones")
search_button = driver.find_element("xpath","//div[@class = 'nav-search-submit nav-sprite']")
search_button.click()
mobiles = driver.find_elements("xpath","//div[@class='puisg-row']//h2//span")
for mobile in mobiles:
    file.write(mobile.get_attribute("innerHTML"))
    file.write("\n")
