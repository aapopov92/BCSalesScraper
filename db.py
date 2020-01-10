import logging
import sqlite3
from sqlite3 import Error


class DB:
    def __init__(self, db_file):
        self.logger = logging.getLogger(__name__)
        self.db_file = db_file
        self.initialize()

    def initialize(self) -> None:
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.logger.info(
                f"Verified connection to {self.db_file} {sqlite3.version} sqlite instance"
            )
        except Error as e:
            self.logger.error(
                f"Failed to connect to {self.db_file} {sqlite3.version} sqlite instance: {e}"
            )
            return
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "DROP TABLE IF EXISTS products"
            )
            cursor.execute(
                f"CREATE TABLE products (id string UNIQUE NOT NULL, discount string, price srtring, brand string, name string, url string, image string)"
            )
            self.logger.info(
                f"Products table is present in {self.db_file}"
            )
        except Error as e:
            self.logger.error(
                f"Failed to create table products in {self.db_file} {sqlite3.version} sqlite instance: {e}"
            )
        finally:
            if cursor:
                cursor.close()

    def write(self, products: list) -> None:
        try:
            cursor = self.conn.cursor()
            cursor.executemany("INSERT OR REPLACE INTO products values (?,?,?,?,?,?,?)", products)
            self.conn.commit()
        except Exception as e:
            self.logger.error(
                f"Failed to write products to {self.db_file}: {e}"
            )
        else:
            self.logger.info(
                f"Successfully wrote {len(products)} products to {self.db_file}"
            )
        finally:
            if cursor:
                cursor.close()
        
