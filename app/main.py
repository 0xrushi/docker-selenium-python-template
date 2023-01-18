from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)

browser.get('https://www.youtube.com')

