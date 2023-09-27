import time
from selenium import webdriver

profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 0)

driver = webdriver.Firefox(firefox_profile=profile)
url = 'https://digikala.com/users/login'

def getUrl(url):
    driver.get(url)
    time.sleep(2)
    driver.close()
    pass

getUrl(url)
