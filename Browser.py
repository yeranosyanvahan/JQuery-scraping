from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
class BROWSER:
    def jquery(self):
        with open('jquery.js','r') as file:
            BROWSER.browser.execute_script(file.read())
        with open('functions.js','r') as file:
            BROWSER.browser.execute_script(file.read())
    def url(self, url):
        BROWSER.browser.get(url)
    def __init__(self, url="https://google.com",headless=False,proxy=""):
        try:
            BROWSER.browser.get(url)
        except:
            Ops={}
            if(proxy!=""):
                prox = Proxy()
                prox.proxy_type = ProxyType.MANUAL
                prox.http_proxy = proxy

                capabilities = webdriver.DesiredCapabilities.CHROME
                prox.add_to_capabilities(capabilities)
                Ops['desired_capabilities']=capabilities
                
            options=webdriver.FirefoxOptions()
            options.headless=headless
            try:
             Ops['executable_path']=GeckoDriverManager().install()
             Ops['options']=options
             browser = webdriver.Firefox(**Ops)
            except:
             Ops['executable_path']=ChromeDriverManager().install()
             browser= webdriver.Chrome(**Ops)
            
            browser.get(url)
            BROWSER.browser=browser
        self.jquery()
    def __call__(self,string):
        return BROWSER.browser.execute_script(string)