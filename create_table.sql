CREATE DATABASE data_warehouse;

USE data_warehouse;

-- Products
CREATE TABLE products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(255),
    Category VARCHAR(255)
);

-- Customers
CREATE TABLE customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerName VARCHAR(255),
    Region VARCHAR(255)
);

-- Time
CREATE TABLE time (
    TimeID INT AUTO_INCREMENT PRIMARY KEY,
    Date DATE,
    Year INT,
    Month INT,
    Day INT
);

-- Sales
CREATE TABLE sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,
    ProductID INT,
    CustomerID INT,
    TimeID INT,
    Quantity INT,
    TotalSales FLOAT,
    FOREIGN KEY (ProductID) REFERENCES products(ProductID),
    FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID),
    FOREIGN KEY (TimeID) REFERENCES time(TimeID)
);
