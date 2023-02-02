import os

from selenium import webdriver


class BasePage:

    def __init__(self):
        self.options = self.set_chrome_options()
        self.browser = self._init_webdriver()

    def _init_webdriver(self):
        return webdriver.Chrome(options=self.options)

    def set_chrome_options(self):
        options = webdriver.ChromeOptions()
        directory = os.path.join(os.path.abspath(os.curdir), "test_ui", "tests")
        prefs = {"download.default_directory": directory}
        options.add_experimental_option("prefs", prefs)
        return options
