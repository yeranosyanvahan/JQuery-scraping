from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class BROWSER:
    def jquery(self):
        with open('jquery.js','r') as file:
            self.browser.execute_script(file.read())
        with open('functions.js','r') as file:
            self.browser.execute_script(file.read())
    def url(self, url):
        self.browser.get(url)
    def __init__(self, url="https://google.com"):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(url)
        self.browser=browser
        self.jquery()
    def __call__(self,string):
        return self.browser.execute_script(string)
    def __del__(self):
        print("Quiting the Browser")
        self.browser.quit()