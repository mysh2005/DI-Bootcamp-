-- Database: dvdrental

-- DROP DATABASE IF EXISTS dvdrental;

CREATE DATABASE dvdrental
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

SELECT * FROM customer; 

SELECT first_name || ' ' || last_name as full_name FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer order by first_name desc;

SELECT film_id, title, description, release_year, rental_rate FROM film order by rental_rate asc;

SELECT address, phone FROM address where district ='Texas';

SELECT description FROM film where film_id = 15 or film_id = 150;

SELECT EXISTS (SELECT  film_id, title, description, length, rental_rate FROM  film WHERE title = 'Ace Goldfinger');

SELECT * FROM film order by rental_rate desc limit 10;

SELECT * FROM film order by rental_rate desc fetch next 10 rows only;

SELECT last_name, first_name, amount, payment_date FROM customer
LEFT JOIN payment ON customer.customer_id = payment.customer_id order by customer.customer_id;

SELECT 
  film.film_id, 
  film.title, 
  inventory.inventory_id 
FROM 
  film 
  LEFT JOIN inventory ON inventory.film_id = film.film_id 
WHERE inventory.inventory_id is null 
ORDER BY 
  film.title;

SELECT city.city_id, city.city, country.country FROM city 
LEFT JOIN country ON city.country_id = country.country_id;

