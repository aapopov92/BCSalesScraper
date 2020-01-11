#!/usr/bin/env python3
"""Main file for parser module. Parses backcountry.com desired category and saves results to local db
Author(s): Oleksii Popov (aapopov@i.ua)

Attributes:
    BASE_URL (str): Base site URL. Without / at the end
    DATABASE (str): Path to the database
    URLS_TO_PARSE (LIST): List of pages to parse
    PARSE_INTERVAL (INT): Interval between parsings, minutes
"""
import logging
from time import sleep
from db import DB
from scrapper import Scrapper

BASE_URL = "https://www.backcountry.com"
URLS_TO_PARSE = ["/paddle?show=all"]
DATABASE = "products.db"
PARSE_INTERVAL = 30


def init_logger():
    """Initialises logger with default parameters
    
    Returns:
        Logger: Logger for main module
    """
    logging.basicConfig(
        filename="log.txt",
        filemode="a",
        format="%(asctime)s | %(name)-10s | %(levelname)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO,
    )
    return logging.getLogger(__name__)


if __name__ == "__main__":
    logger= init_logger()
    db = DB(DATABASE)
    scrapper = Scrapper()
    logger.info("Service started")

    # Main loop:
    while True:
        for url in URLS_TO_PARSE:
            logger.info(f"Scraping {url}")
            products = scrapper.scrape(BASE_URL, url)  # Swiper swiping!
            logger.info(f"Found {len(products)} products")

            new = db.which_product_is_new(products)
            if new:
                logger.info(f"Found {len(new)} new products:")
                for product in new:
                    logger.info(product)

            db.write(products)
            logger.debug(f"{products}")
        sleep(PARSE_INTERVAL * 60)
