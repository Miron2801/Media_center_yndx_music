from selenium import webdriver
import time
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://www.youtube.com/watch?v=O3ElohqHEzQ")
elem = driver.find_element_by_class_name("ytp-play-button")
elem.click()