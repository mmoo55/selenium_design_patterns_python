from selenium import webdriver

class Browser:

    driver = None

    def goTo(self, url, navigator):

        if navigator == "Chrome":
            Browser.driver = webdriver.Chrome()

        elif navigator == "Firefox":
            Browser.driver = webdriver.Firefox()

        elif navigator == "Safari":
            Browser.driver = webdriver.Safari()

        Browser.driver.get(url)

    def titulo(self):
        return Browser.driver.title

    def close(self):
        Browser.driver.close()