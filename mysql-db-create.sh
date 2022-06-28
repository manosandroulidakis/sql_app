#!/bin/bash

mysql -u root
GRANT ALL PRIVILEGES ON *.* TO 'db_user'@'localhost' IDENTIFIED BY 'P@s$w0rd123!';
\q
mysql -u db_user -ppassword

CREATE DATABASE db_music;
use db_music;
CREATE TABLE cd (title VARCHAR(50) NOT NULL,
		duration FLOAT(50) NOT NULL,
		year_of_release FLOAT(50) NOT NULL,
		price FLOAT(50) NOT NULL);

CREATE TABLE VINYL (title VARCHAR(50) NOT NULL,
		duration FLOAT(50) NOT NULL,
		rotation_speed FLOAT(50) NOT NULL,
		year_of_release FLOAT(50) NOT NULL,		
		price FLOAT(50) NOT NULL);

CREATE TABLE User (name VARCHAR(50) NOT NULL,
		surname VARCHAR(50) NOT NULL,
		email VARCHAR(50) NOT NULL,
		physical_address VARCHAR(50) NOT NULL);

insert into cd(title,duration,year_of_release,price) VALUES ('soft machine', 44.45, 1981, 10);
insert into cd(title,duration,year_of_release,price) VALUES ('led zeppelin IV', 43.42, 1981, 10);

insert into vinyl(title, duration, rotation_speed, year_of_release,price) VALUES ('dark side of the moon', 45.45, 78, 1973, 10);
insert into vinyl(title, duration, rotation_speed, year_of_release,price) VALUES ('in the court of the crimson king', 46.42, 45, 1969, 10);

insert into user(name, surname, email, physical_address) VALUES ('john', 'doe', 'john_doe@johnmail.com', '34, John Doe St');
