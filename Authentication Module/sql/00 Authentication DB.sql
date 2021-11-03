DROP DATABASE IF EXISTS Authentication;
CREATE DATABASE Authentication;
USE Authentication;

CREATE TABLE Users (
	userID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    firstName VARCHAR(30) NOT NULL,
    lastName VARCHAR(30) NOT NULL,
    role INT(3) NOT NULL,
	password VARCHAR(30) NOT NULL
);

