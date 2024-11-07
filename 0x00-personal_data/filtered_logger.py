#!/usr/bin/env python3
"""
A module for handling logging of personal data with PII obfuscation.
"""

import re
import logging
from typing import List
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Return the obfuscated log message."""
    for field in fields:
        message = re.sub(fr"{field}=[^;]+", f"{field}={redaction}", message)
    return message

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        original_message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, original_message, self.SEPARATOR)

def get_logger() -> logging.Logger:
    """Create and configure the logger."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(handler)
    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to the database using environment variables."""
    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME")
    )

def main():
    """Retrieve and display user records with sensitive data obfuscated."""
    logger = get_logger()
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT name, email, phone, ssn, password, ip, last_login, user_agent FROM users;")
    for row in cursor:
        message = ("name={}; email={}; phone={}; ssn={}; password={}; ip={}; last_login={}; user_agent={}"
                   .format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        logger.info(message)
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
