create database EasyCart;
use EasyCart;

CREATE TABLE `Users` (
  `user_id` varchar(20) PRIMARY KEY,
  `user_name` varchar(50),
  `passcode` varchar(50),
  `email` varchar(50) UNIQUE,
  `phoneNo` varchar(10)
);

CREATE TABLE `Seller` (
  `Seller_id` varchar(20) PRIMARY KEY,
  `user_name` varchar(50),
  `passcode` varchar(50),
  `email` varchar(50) UNIQUE,
  `phoneNo` varchar(10)
);

CREATE TABLE `Customer` (
  `Customer_id` varchar(20) PRIMARY KEY,
  `user_name` varchar(50),
  `passcode` varchar(50),
  `email` varchar(50),
  `phoneNo` varchar(10)
);

CREATE TABLE `Product` (
  `product_id` varchar(20) PRIMARY KEY,
  `product_name` varchar(50),
  `product_description` varchar(200),
  `Seller_id` varchar(20),
  `Category` varchar(50),
  `cost` double,
  `quantity` int,
  `rating` double,
  `totalreviews` int
);

CREATE TABLE `SellerInventory` (
  `user_id` varchar(20),
  `product_id` varchar(20),
  `quantity` double,
  `last updated` varchar(50),
  PRIMARY KEY (`user_id`, `product_id`)
);

CREATE TABLE `Cart` (
  `cart_id` varchar(20) PRIMARY KEY,
  `product_name` varchar(50),
  `product_id` varchar(20),
  `customer_id` varchar(20),
  `billamount` double,
  `dateadded` varchar(20),
  `expectdelivery` varchar(20)
);

CREATE TABLE `Orders` (
  `order_id` varchar(20) PRIMARY KEY,
  `user_id` varchar(20),
  `product_id` varchar(20),
  `order_date` date,
  `cost` double,
  `PaymentMode` varchar(50),
  `status` varchar(50)
);

CREATE TABLE `Feedback` (
  `order_id` varchar(20) PRIMARY KEY,
  `product_id` varchar(20),
  `user_id` varchar(20),
  `fdate` date,
  `ratingpoints` double
);

CREATE TABLE `Category` (
  `cat_id` varchar(20) PRIMARY KEY,
  `category_name` varchar(50)
);

SELECT * FROM `Product`;

INSERT INTO `Category` VALUES(1,"Automative and PowerSports");
INSERT INTO `Category` VALUES(2,"Baby Products");
INSERT INTO `Category` VALUES(3,"Beauty");
INSERT INTO `Category` VALUES(4,"Books");
INSERT INTO `Category` VALUES(5,"Camera and Photo");
INSERT INTO `Category` VALUES(6,"Consumer Electronics");
INSERT INTO `Category` VALUES(7,"Entertainment");
INSERT INTO `Category` VALUES(8,"Fashion and Clothing");
INSERT INTO `Category` VALUES(9,"Fine Art");
INSERT INTO `Category` VALUES(10,"Grocery and Food");
INSERT INTO `Category` VALUES(11,"Health and Personal Care");
INSERT INTO `Category` VALUES(12,"Industrial and Scientific");
INSERT INTO `Category` VALUES(13,"Music");
INSERT INTO `Category` VALUES(14,"Office Products");
INSERT INTO `Category` VALUES(15,"Outdoors");
INSERT INTO `Category` VALUES(16,"Software");
INSERT INTO `Category` VALUES(17,"Shoes");
INSERT INTO `Category` VALUES(18,"Sports");
INSERT INTO `Category` VALUES(21,"Others");
INSERT INTO `Category` VALUES(19,"Home Decoration");
INSERT INTO `Category` VALUES(20,"Covid Emergencies");

CREATE TABLE `SellerOrderHistory` (
  `user_id` varchar(20),
  `product_id` varchar(20),
  `order_id` varchar(20) PRIMARY KEY,
  `orderselldate` date,
  `paymentmode` varchar(50)
);

INSERT INTO `Users` VALUES (1,"Admin","Admin","Admin",0123456789);
