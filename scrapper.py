"""Scrapper module. Implenets scraping logic for backcountry.com
Author(s): Oleksii Popov (aapopov@i.ua)
"""
import requests
import logging
from bs4 import BeautifulSoup


class Scrapper(object):
    """Scrapper class
    
    Attributes:
        logger (Logger): Logger instance
    """
    
    def __init__(self):
        """Init. Only logger here :)
        """
        self.logger = logging.getLogger(__name__)

    def scrape(self, base_url, page):
        """Main method. Scrapes page from backcountry.com and returns list of products
        
        Args:
            base_url (str): Base site URL, without /. E.g. "http://www.backcountry.com"
            page (str): Page to scrape, with / at the start, e.g. '/whitewater-paddles'
        
        Returns:
            List: List of products dicts:
            {'id': str, 
            'discount': str, 
            price': str, 
            'brand': str, 
            'name': str,
            'link': str,
            'image': str
            }
        """
        products = list()
        diff = list()
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

            # JS-generated content for some products. Change image url attribute in case of AttributeError.
            try:
                image = product.find("img")["src"]
            except KeyError:
                image = product.find("img")["data-src"]

            # No pricing tag in case of out of stock
            try:
                price = (
                    product.find("span", {"class": "ui-pl-pricing-low-price"}).text
                    if discount
                    else product.find(
                        "span", {"class": "ui-pl-pricing-high-price"}
                    ).text
                )
            except AttributeError:
                price = "Temporarily Out Of Stock"

            products.append(
                {
                    "id": uuid,
                    "discount": discount,
                    "price": price,
                    "brand": brand,
                    "name": name,
                    "url": base_url + link,
                    "image": "https:" + image.replace("medium", "1200"),
                }
            )
        next_page = soup.find("li", {"class": "pag-next"})
        # Recursively scrape all pages in case pagination found
        if next_page:
            return products + self.scrape(base_url, next_page.find("a")["href"])
        return products
