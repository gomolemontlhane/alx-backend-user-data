# 0x00. Personal Data

## Description

This project involves working with sensitive personal data and learning how to handle, log, and secure Personally Identifiable Information (PII) effectively. Key goals include obfuscating PII fields in logs, encrypting passwords, authenticating databases with environment variables, and implementing logging practices that respect data privacy.

## Learning Objectives

By the end of this project, you should be able to:

- Identify examples of Personally Identifiable Information (PII).
- Implement log filters to obfuscate PII fields in log messages.
- Encrypt passwords and validate password inputs securely.
- Authenticate to a database using environment variables.

## Resources

- What Is PII, non-PII, and Personal Data?
- Python logging documentation
- bcrypt package for password hashing
- Logging to Files, Setting Levels, and Formatting

## Requirements

- Python 3.7 on Ubuntu 18.04 LTS
- Code must conform to pycodestyle (version 2.5)
- All files must be executable, end with a new line, and use type annotations.
- Complete and meaningful documentation for all modules, classes, and functions.

## Project Tasks

### Task 0: Regex-ing

- Goal: Write filter_datum() to obfuscate specified fields in a log message.
- Details:
  Parameters: fields (fields to obfuscate), redaction (replacement text), message (log message), and separator (character separating fields).
  Should use a regex to replace field values, utilizing re.sub.

### Task 1: Log Formatter

- Goal: Implement RedactingFormatter class that applies PII field obfuscation in log messages.
- Details:
  Inherit from logging.Formatter and override the format method.
  Format log records using filter_datum.

### Task 2: Create Logger

- Goal: Implement get_logger() function that returns a configured logging.Logger.
- Details:
  Use RedactingFormatter as formatter with StreamHandler.
  Define PII_FIELDS constant containing fields from user_data.csv that are considered PII.

### Task 3: Connect to Secure Database

- Goal: Implement get_db() function to connect securely to the database.
- Details:
  Use environment variables for database credentials (PERSONAL_DATA_DB_USERNAME, PERSONAL_DATA_DB_PASSWORD, PERSONAL_DATA_DB_HOST, and PERSONAL_DATA_DB_NAME).
  Use mysql-connector-python for database connection.

### Task 4: Read and Filter Data

- Goal: Implement main() function to retrieve and display rows from the users table.
- Details:
  Connect to the database using get_db().
  Log each row with obfuscation of PII fields using RedactingFormatter.

## Usage

1. Install required packages:
   bash

```bash
pip3 install bcrypt mysql-connector-python
```

2. Set environment variables for database credentials:
   bash

```bash
export PERSONAL_DATA_DB_USERNAME='your_username'
export PERSONAL_DATA_DB_PASSWORD='your_password'
export PERSONAL_DATA_DB_HOST='your_host'
export PERSONAL_DATA_DB_NAME='your_database'
Run the project using the main script:
```

```bash
./filtered_logger.py
```

##Project Structure

```bash
.
├── filtered_logger.py     # Contains all main implementations and functions
├── main.py                # Script for testing individual tasks
└── README.md              # Project documentation
```

## License

This project is part of the ALX Back-end curriculum and is licensed for educational purposes.
