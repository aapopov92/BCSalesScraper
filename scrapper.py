import requests
import logging
from bs4 import BeautifulSoup


class Scrapper(object):
    """Scrapper class"""
    def __init__(self):
        super(Scrapper, self).__init__()
        self.logger = logging.getLogger(__name__)

    def scrape(self, base_url, page):
        products = []
        url = base_url + page
        self.logger.debug(f"Scraping {url}")
        html = requests.get(url).text
        soup = BeautifulSoup(html, "html.parser")
        products_tags = soup.findAll("div", {"class": "product"})
        for product in products_tags:
            uuid = product["data-product-id"]
            try:
                discount = product.find("span", {"class": "discount-amount-text"}).text
            except AttributeError:
                discount = None
            brand = product.find("span", {"class": "ui-pl-name-brand"}).text
            name = product.find("span", {"class": "ui-pl-name-title"}).text
            link = product.find("a", {"class": "ui-pl-link"})["href"]
            try:
                price = (
                    product.find("span", {"class": "ui-pl-pricing-low-price"}).text
                    if discount
                    else product.find("span", {"class": "ui-pl-pricing-high-price"}).text
                )
            except AttributeError:
                price = 'Temporarily Out Of Stock'
            products.append(
                {
                    "id": uuid,
                    "discount": discount,
                    "price": price,
                    "brand": brand,
                    "name": name,
                    "url": link,
                }
            )
        next_page = soup.find("li", {"class":"pag-next"})
        if next_page:
            return products + self.scrape(base_url, next_page.find("a")["href"])
        return products
