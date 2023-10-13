-- create user table with id, name, email column

-- create table
CREATE TABLE IF NOT EXISTS users
       (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255) )
