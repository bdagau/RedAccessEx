from pip._vendor import requests


class PastebinApiHandler:

    def __init__(self):
        self.url = self.set_url()
        self.payload = {'api_dev_key': '2XBjhk_XFVWMUmfayVfs_XUmnTvGns2P'}

    def set_url(self):
        base_url = "https://pastebin.com/api/api_post.php"
        return base_url

    def create_new_paste(self, text):
        self.payload['api_option'] = 'paste'
        self.payload['api_paste_code'] = text
        response = requests.post(self.url, data=self.payload)
        return response
