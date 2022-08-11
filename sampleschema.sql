CREATE TABLE IF NOT EXISTS Supplying_facilities(
    id INT AUTO_INCREMENT PRIMARY KEY,
    Sname VARCHAR(20),
    Regno VARCHAR(10),
    Sphone VARCHAR(10),
    Semail VARCHAR(30),
    Saddress VARCHAR(30),
    Sdistrict VARCHAR(30),
    SupplierID INT ,
    iscomplete INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS Store(
    id INT AUTO_INCREMENT PRIMARY KEY,
    SupplierID INT,
    Storename VARCHAR(20),
    Storedistrict VARCHAR(30),
    Storeward VARCHAR(30),
    Storestreet VARCHAR(30),
);

CREATE TABLE IF NOT EXISTS Customer_facility(
    id INT AUTO_INCREMENT PRIMARY KEY,
    HFid INT,
    HFtype VARCHAR(50),
    HFname VARCHAR(30),
    HFemail VARCHAR(30),
    HFdistrict VARCHAR(30),
    HFphone VARCHAR(10),
);

CREATE TABLE IF NOT EXISTS PCatalogue(
    id INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT,
    Pname VARCHAR(30),
    Pcategory VARCHAR(40),
    Psubcategory VARCHAR(40),
    Pbrand VARCHAR(30),
    Pdescription CHAR(50),
    Pimage VARCHAR(30),
    Pprice DECIMAL(10,2) ,
    discount VARCHAR(3),
    discountpercent INT ,
    SupplierID INT,
);

CREATE TABLE IF NOT EXISTS Users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    SupplierID INT,
    Uname VARCHAR(30),
    UserID INT,
    Uphone VARCHAR(10),
    Uemail VARCHAR(20),
    Usertype VARCHAR(50),
    HFid int,
    Regno VARCHAR(10),
);




