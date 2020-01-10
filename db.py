import logging
import sqlite3
from sqlite3 import Error


class DB:
    def __init__(self, db_file):
        self.logger = logging.getLogger(__name__)
        self.db_file = db_file
        self.initialize()
        

    def initialize(self):
        try:
            conn = sqlite3.connect(self.db_file)
            self.logger.info(f"Verified connection to {self.db_file} {sqlite3.version} sqlite instance")
        except Error as e:
            self.logger.error(f"Failed to connect to {self.db_file} sqlite instance: {e}")
        finally:
            if conn:
                conn.close()

