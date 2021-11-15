USE PHPDB;

CREATE TABLE IF NOT EXISTS Items (
    itemID INT(5) AUTO_INCREMENT NOT NULL PRIMARY KEY,
    itemName VARCHAR(255) NOT NULL,
    itemPrice Decimal(7,2) NOT NULL,
    itemQuantity int(10) NOT NULL
);