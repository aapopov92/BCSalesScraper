"""Database module
Author(s): Oleksii Popov (aapopov@i.ua)
"""
import logging
import sqlite3
from sqlite3 import Error


class DB:
    """Databse class
    
    Attributes:
        conn (sqlite3.Connection): DB connection object
        db_file (str): Path to DB file
        logger (Logger): DB logger instance
    """
    
    def __init__(self, db_file):
        """Summary
        
        Args:
            db_file (str): Path to DB file
        """
        self.logger= logging.getLogger(__name__)
        self.db_file: str = db_file
        self.initialize()

    def initialize(self) -> None:
        """DB intialisation:
        1. Initialise connection
        2. DROP TABLE if exists
        3. Create products table
        
        Returns:
            None
        """
        try:
            self.conn: sqlite3.Connection = sqlite3.connect(self.db_file)
            self.logger.info(
                f"Verified connection to {self.db_file} {sqlite3.version} sqlite instance"
            )
        except Error as e:
            self.logger.error(
                f"Failed to connect to {self.db_file} {sqlite3.version} sqlite instance: {e}"
            )
            return
        try:
            cursor: sqlite3.Cursor = self.conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS products")
            cursor.execute(
                f"CREATE TABLE products (id string UNIQUE NOT NULL, discount string, price srtring, brand string, name string, url string, image string)"
            )
            self.logger.info(f"Products table is present in {self.db_file}")
        except Error as e:
            self.logger.error(
                f"Failed to create table products in {self.db_file} {sqlite3.version} sqlite instance: {e}"
            )
        finally:
            if cursor:
                cursor.close()

    def write(self, products: list) -> None:
        """Write to db
        
        Args:
            products (list): List of dicts to write to db. See scrapper module for dict structure.
        """
        try:
            cursor = self.conn.cursor()
            cursor.executemany(
                "INSERT OR REPLACE INTO products values (?,?,?,?,?,?,?)",
                [tuple(product.values()) for product in products],
            )
            self.conn.commit()
        except Exception as e:
            self.logger.error(f"Failed to write products to {self.db_file}: {e}")
        else:
            self.logger.info(
                f"Successfully wrote {len(products)} products to {self.db_file}"
            )
        finally:
            if cursor:
                cursor.close()

    def which_product_is_new(self, products: list) -> list:
        """Returns products, that are not present in DB
        
        Args:
            products (list): List of dicts to check. See scrapper module for dict structure.
        
        Returns:
            list: List of new products
        """
        # TODO: Implement logic to return products that were in DB, but got on sale
        diff: list = list()
        try:
            cursor = self.conn.cursor()
            for product in products:
                present = cursor.execute(
                    f"SELECT * FROM products WHERE id = '{product['id']}'"
                ).fetchone()
                if not present:
                    diff.append(product)
        except Exception as e:
            self.logger.error(
                f"Failed to read product {product['id']} from {self.db_file}: {e}"
            )
        finally:
            if cursor:
                cursor.close()
        return diff
