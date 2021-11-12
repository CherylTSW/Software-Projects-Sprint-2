DROP DATABASE IF EXISTS PHPDB;
CREATE DATABASE PHPDB;
USE PHPDB;

CREATE TABLE Users (
	userID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    role INT(3) NOT NULL,
	password VARCHAR(30) NOT NULL
);

CREATE TABLE Sales (
    salesID INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    salesItem VARCHAR(255) NOT NULL,
    salesAmount Decimal(7,2) NOT NULL
);

INSERT INTO Users (username, firstName, lastName, role, password) VALUES ("test", "test", "test", 1, "test");

INSERT INTO Sales (salesItem, salesAmount) VALUES ("Item No.1", 10.00);

INSERT INTO Sales (salesItem, salesAmount) VALUES ("Item No.2", 20.50);

INSERT INTO Sales (salesItem, salesAmount) VALUES ("Item No.3", 200.00);