import requests as rq
import random
import re

class imapi:
    def __init__(self, search):
        self.search = search
        self.image_urls = []
        try:
            response = rq.get(f"https://unsplash.com/s/photos/{search}")
            if response.status_code == 200:
                html_content = response.text
                regex = r"https://images\S+.=80"
                self.image_urls = re.findall(regex, html_content)
        except Exception as e:
            print(f"Error occurred: {e}")

    def single(self):
        if self.image_urls:
            self.url = random.choice(self.image_urls)
            return self

    def __str__(self):
        return str(self.image_urls)

    def download(self):
        try:
            response = rq.get(self.url)
            if response.status_code == 200:
                with open(f"{self.search}.png", 'wb') as file:
                    file.write(response.content)
                return f"{self.search}.png"
            else:
                return "Error while downloading image."
        except Exception as e:
            return f"Error: {e}"

      
