from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
class BROWSER:
    def jquery(self):
        with open('jquery.js','r') as file:
            BROWSER.browser.execute_script(file.read())
        with open('functions.js','r') as file:
            BROWSER.browser.execute_script(file.read())
    def url(self, url):
        BROWSER.browser.get(url)
    def __init__(self, url="https://google.com",headless=False):
        try:
            BROWSER.browser.get(url)
        except:
            options=webdriver.FirefoxOptions()
            options.headless=headless
            browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
            browser.get(url)
            BROWSER.browser=browser
        self.jquery()
    def __call__(self,string):
        return BROWSER.browser.execute_script(string)