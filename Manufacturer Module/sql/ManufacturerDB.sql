USE SPRINT1;

CREATE TABLE MANUFACTURER (
    ManufacturerID INT(10) NOT NULL,
    ManufacturerFirstName nvarchar(25) NULL,
    ManufacturerLastName nvarchar(25) NULL,
    ManufacturerItem nvarchar(30) NULL,
    ManufacturerStreetAddress nvarchar(50) NULL,
    ManufacturerPhoneNumber INT(12) NULL,
    PRIMARY KEY (ManufacturerID)
);