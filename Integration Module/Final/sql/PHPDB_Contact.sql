USE PHPDB;

CREATE TABLE CONTACTMODULE (
    OrderID INT(10) NOT NULL,
    OrderDate NVARCHAR(10) NULL,
    ManufacturerID INT(10) NULL,
    ProductID INT(10) NULL,
    Quantity INT(10) NULL,
    TotalPrice FLOAT(10,2) NULL,
    PRIMARY KEY (OrderID)
);