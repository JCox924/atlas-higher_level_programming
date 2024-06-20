# SQLAlchemy ORM Project

## Overview

This project demonstrates how to use SQLAlchemy ORM to interact with a MySQL database. The project includes scripts to create tables, insert data, and query data from the database. The focus is on creating and manipulating `State` and `City` objects using SQLAlchemy.

## Prerequisites

- Python 3.8+
- MySQL 8.0+
- SQLAlchemy
- MySQLdb (mysqlclient)

## Installation

1. Install Python and MySQL on your system.
2. Install the required Python packages:
    ```sh
    pip3 install SQLAlchemy mysqlclient
    ```

## Files

- `model_state.py`: Defines the `State` class and `Base` instance.
- `model_city.py`: Defines the `City` class.
- `create_tables.py`: Creates the `states` and `cities` tables in the database.
- `14-model_city_fetch_by_state.py`: Prints all `City` objects from the database, sorted by `cities.id`.

## Usage

### Creating Tables

To create the `states` and `cities` tables in the database, run the `create_tables.py` script:

```sh
./create_tables.py <mysql_username> <mysql_password> <database_name>
