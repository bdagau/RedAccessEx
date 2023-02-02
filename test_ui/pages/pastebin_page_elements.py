from selenium.webdriver.common.by import By


class PastebinPageElements:

    def __init__(self, browser):
        self.browser = browser

    def get_new_paste_text_box(self):
        return self.browser.find_element(By.ID, "postform-text")

    def get_category_dropdown(self):
        return self.browser.find_element(By.ID, "select2-postform-category_id-container")

    def get_paste_name_text_box(self):
        return self.browser.find_element(By.ID, "postform-name")

    def get_create_new_paste_button(self):
        return self.browser.find_element(By.XPATH, f"//button[@class='btn -big']")

    def get_search_field(self):
        return self.browser.find_element(By.CLASS_NAME, "select2-search__field")

    def get_category(self, category_name):
        return self.browser.find_element(By.XPATH, f"//li[text()='{category_name}']")

    def get_download_button(self):
        return self.browser.find_element(By.XPATH, "//div/a[text()='download']", )
