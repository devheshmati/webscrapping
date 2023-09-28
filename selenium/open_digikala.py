from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.by import By

# Create a FirefoxOptions object
options = webdriver.FirefoxOptions()

# Create a Proxy object and set its type to 'DIRECT' to specify no proxy
proxy = Proxy()
proxy.proxy_type = ProxyType.DIRECT

# Add the proxy settings to the FirefoxOptions object
options.proxy = proxy

# Create the WebDriver with the specified options
driver = webdriver.Firefox(options=options)
url = 'https://digikala.com/users/login'

try:
    driver.get(url)
    input = driver.find_element(By.NAME, 'username')
    input.send_keys('womoboy')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()
except Exception as e:
    print('error', str(e)) 
