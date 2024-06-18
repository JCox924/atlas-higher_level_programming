# MySQL Database Setup and Advanced Queries

## Overview
This README provides instructions to create a MySQL database `hbtn_0d_2`, a user `user_0d_2` with specific privileges, and demonstrates various SQL queries to manage and interact with the database.

## Prerequisites
- MySQL server installed
- MySQL command-line client

## Basic Setup

### 1. Create Database and User
This script creates the database `hbtn_0d_2` and the user `user_0d_2` with a password `user_0d_2_pwd`. The user is granted only the `SELECT` privilege on the database.

```sql
-- Create the database hbtn_0d_2 if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user user_0d_2 with password user_0d_2_pwd if the user doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to ensure that all changes take effect
FLUSH PRIVILEGES;

