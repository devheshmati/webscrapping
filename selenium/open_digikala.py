import time
from selenium import webdriver

# Create a new FirefoxProfile object.
profile = webdriver.FirefoxProfile()

# Set the network.proxy.type preference to 0 (No proxy).
profile.set_preference("network.proxy.type", 0)

# Create a new FirefoxDriver object, passing in the FirefoxProfile object.
driver = webdriver.Firefox(firefox_profile=profile)

# Open the desired URL.
driver.get("https://digikala.com/users/login")

# Wait for the page to load.
time.sleep(1)

# Close the browser.
driver.close()
