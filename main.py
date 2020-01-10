import logging
from time import sleep
from db import DB
from scrapper import Scrapper

BASE_URL = "https://www.backcountry.com"
URLS_TO_PARSE = ["/paddle?show=all"]
DATABASE = "products.db"


def init_logger():
    logging.basicConfig(
        filename="log.txt",
        filemode="a",
        format="%(asctime)s | %(name)-10s | %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    return logging.getLogger(__name__)


if __name__ == "__main__":
    logger = init_logger()
    logger.info("Starting service")
    db = DB(DATABASE)
    scrapper = Scrapper()
    while True:
        for url in URLS_TO_PARSE:
            logger.info(f"Scraping {url}")
            products = scrapper.scrape(BASE_URL, url)  # Жулик, воруй!
            logger.info(f"Found {len(products)} products")
            db.write([tuple(product.values()) for product in products])
            logger.debug(f"{products}")
        sleep(1600)
