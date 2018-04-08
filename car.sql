/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 5.6.12-log : Database - pydata
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
/*Table structure for table `auto_home_car_brand` */

CREATE TABLE `auto_home_car_brand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `brandid` int(11) NOT NULL DEFAULT '0',
  `name` varchar(50) NOT NULL,
  `bfirstletter` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=191 DEFAULT CHARSET=utf8;

/*Table structure for table `auto_home_car_model` */

CREATE TABLE `auto_home_car_model` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `series_id` int(11) NOT NULL DEFAULT '0',
  `year_id` int(11) NOT NULL DEFAULT '0',
  `year_name` varchar(50) NOT NULL,
  `model_id` int(11) DEFAULT NULL,
  `model_name` varchar(50) DEFAULT NULL,
  `model_state` varchar(50) DEFAULT NULL,
  `min_price` varchar(50) DEFAULT NULL,
  `max_price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx` (`series_id`,`year_id`,`model_id`)
) ENGINE=InnoDB AUTO_INCREMENT=29180 DEFAULT CHARSET=utf8;

/*Table structure for table `auto_home_car_series` */

CREATE TABLE `auto_home_car_series` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `brand_id` int(11) NOT NULL DEFAULT '0',
  `factory_id` int(11) NOT NULL DEFAULT '0',
  `factory_name` varchar(50) NOT NULL,
  `series_id` int(11) DEFAULT NULL,
  `series_name` varchar(50) DEFAULT NULL,
  `series_state` varchar(50) DEFAULT NULL,
  `series_order` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx` (`brand_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1765 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;