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

DROP TABLE public.items;

CREATE TABLE items(
 items_id SERIAL PRIMARY KEY,
 items_type VARCHAR (50) NOT NULL,
 items_price SMALLINT NOT NULL
)

DROP TABLE public.customers;

CREATE TABLE customers(
 customers_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL
)

INSERT INTO items (items_id, items_type, items_price)
VALUES('1','Small Desk',100),
('2','Large Desk',300),
('3','Fan',80);

INSERT INTO customers (customers_id, first_name, last_name)
VALUES('1','Greg','Jones'),
('2','Sandra','Jones'),
('3','Scott','Scott'),
('4','Trevor','Green'),
('5','Melanie','Johnson');

select * from items; 
select * from items where items_price > 80; 
select * from items where items_price <= 300; 

select * from customers where last_name = 'Smith'; 
select * from customers where last_name = 'Jones'; 
select * from customers where first_name != 'Scott'; 