CREATE DATABASE mall
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE mall;

CREATE TABLE products(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    price DOUBLE
);

INSERT INTO products(name,price)
VALUES
('苹果手机',5999),
('华为手机',4999),
('小米手机',3999);

CREATE TABLE orders(
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    quantity INT
);