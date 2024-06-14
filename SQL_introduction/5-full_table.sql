-- 5-full_table.sql
-- This script prints the description of first_table from hbtn_0c_0
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMS
WHERE TABLE_NAME = 'first_table' AND TABLE_SCHEMA = DATABASE();
