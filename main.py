import requests
from bs4 import BeautifulSoup as bs

class Scrape:
    def __init__(self, url, tag, class_):
        self.url = url
        self.tag = tag
        self.class_ = class_

    def make_connection(self):
        html_text = requests.get(self.url).text
        self.soup = bs(html_text, 'lxml')
        self.items = self.soup.find_all(self.tag, self.class_)

    def show_items(self, tag, class_, price_tag, price_class):
        self.make_connection()
        for index, item in enumerate(self.items):
            item_title = item.find(tag, class_).text
            item_price = item.find(price_tag, price_class).text

            with open(f'post/{index}.txt', 'w') as f:
                f.write(f"Title is:  {item_title.strip()}  and: {item_price.strip()} rub")


# obj = Scrape('https://boxx.ru/catalog/shkafy-i-stellazhi/vse-shkafy/shkafy-raspashnye_1/', 'div', 'inner_wrap TYPE_1')
# obj.show_items('div', 'item-title', 'span', 'price_value')
