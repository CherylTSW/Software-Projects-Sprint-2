CREATE DATABASE IF NOT EXISTS PHPDB;
USE PHPDB;

CREATE TABLE IF NOT EXISTS Users (
	userID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    role INT(3) NOT NULL,
	password VARCHAR(30) NOT NULL
);

INSERT INTO Users (username, firstName, lastName, role, password)
VALUES ("test", "test", "test", 1, "test");