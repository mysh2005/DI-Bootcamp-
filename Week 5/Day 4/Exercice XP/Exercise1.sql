-- Database: public

-- DROP DATABASE IF EXISTS public;

CREATE DATABASE public
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

SELECT * FROM items order by items_price;

SELECT * FROM items where items_price >= 80 order by items_price desc;

SELECT first_name, last_name FROM customers order by first_name limit 3;

SELECT last_name FROM customers order by last_name desc;


