from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

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
            try:
             browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
            except:
             browser= webdriver.Chrome(ChromeDriverManager().install())
            
            browser.get(url)
            BROWSER.browser=browser
        self.jquery()
    def __call__(self,string):
        return BROWSER.browser.execute_script(string)