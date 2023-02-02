from test_ui.pages.pastebin_page import PasteBinPage

test_data = {
    "paste_data": {
        "paste_text": "this is a test for Red Access 1234!@#$",
        "category": "Food",
        "paste_name": "test name"
    },
    "expected_results": "this is a test for Red Access 1234!@#$"
}


def test_add_and_download_paste():
    pastebin_page = PasteBinPage()
    pastebin_page.add_new_paste_and_save(**test_data["paste_data"])
    pastebin_page.download_and_verify_paste(test_data["expected_results"])
