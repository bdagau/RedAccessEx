from tests_api.pastebin_api_handler.pastebin_api_handler import PastebinApiHandler


def test_create_and_get_new_paste():
    api_handler = PastebinApiHandler()
    api_handler.create_new_paste("test")
