from test_ui.pages.base_page import BasePage
from test_ui.pages.download_handler import last_file_downloaded
from test_ui.pages.pastebin_page_elements import PastebinPageElements


class PasteBinPage(BasePage):

    def __init__(self):
        super().__init__()
        self.browser.get("https://pastebin.com/")
        self.elements = PastebinPageElements(self.browser)

    def select_paste_category(self, category):
        self.elements.get_category_dropdown().click()
        self.elements.get_search_field().send_keys(category)
        self.elements.get_category(category).click()

    def add_new_paste_and_save(self, paste_text, category, paste_name):
        self.elements.get_new_paste_text_box().send_keys(paste_text)
        self.select_paste_category(category)
        self.elements.get_paste_name_text_box().send_keys(paste_name)
        self.elements.get_create_new_paste_button().click()

    def download_and_verify_paste(self, expected_results):
        self.elements.get_download_button().click()
        file = last_file_downloaded(self.options.experimental_options["prefs"]['download.default_directory'])
        with open(file, 'r') as file:
            data = file.read().replace('\n', '')
        assert data == expected_results
