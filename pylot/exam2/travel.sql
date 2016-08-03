-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 127.0.0.1    Database: travel
-- ------------------------------------------------------
-- Server version	5.5.42

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `buddies`
--

DROP TABLE IF EXISTS `buddies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `buddies` (
  `user_id` int(11) NOT NULL,
  `trip_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`user_id`,`trip_id`),
  KEY `fk_users_has_trips_trips1_idx` (`trip_id`),
  KEY `fk_users_has_trips_users_idx` (`user_id`),
  CONSTRAINT `fk_users_has_trips_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_trips_trips1` FOREIGN KEY (`trip_id`) REFERENCES `trips` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buddies`
--

LOCK TABLES `buddies` WRITE;
/*!40000 ALTER TABLE `buddies` DISABLE KEYS */;
INSERT INTO `buddies` VALUES (1,15,'2016-07-27 17:38:01','2016-07-27 17:38:01'),(2,17,'2016-07-27 17:41:44','2016-07-27 17:41:44'),(2,18,'2016-07-27 17:49:56','2016-07-27 17:49:56'),(3,16,'2016-07-27 18:11:16','2016-07-27 18:11:16'),(3,17,'2016-07-27 18:00:38','2016-07-27 18:00:38');
/*!40000 ALTER TABLE `buddies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trips`
--

DROP TABLE IF EXISTS `trips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `depart` varchar(255) DEFAULT NULL,
  `arrive` varchar(255) DEFAULT NULL,
  `user_id` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips`
--

LOCK TABLES `trips` WRITE;
/*!40000 ALTER TABLE `trips` DISABLE KEYS */;
INSERT INTO `trips` VALUES (15,'London','Tour the city','08/04/2016','08/17/2016','2','2016-07-27 17:01:50','2016-07-27 17:01:50'),(16,'South Africa','Play with the sharks','08/11/2016','08/25/2016','2','2016-07-27 17:03:32','2016-07-27 17:03:32'),(17,'Texas','Leave as fast as possible','08/17/2016','08/30/2016','1','2016-07-27 17:11:03','2016-07-27 17:11:03'),(18,'Charleston','Beach time!','08/10/2016','08/22/2016','1','2016-07-27 17:34:34','2016-07-27 17:34:34'),(19,'Belize','Just... Because','08/11/2016','08/24/2016','1','2016-07-27 17:40:39','2016-07-27 17:40:39'),(20,'North Pole','Be cold for a while','08/17/2016','09/19/2016','1','2016-07-27 17:40:55','2016-07-27 17:40:55'),(21,'Pacific Ocean','Float','08/08/2016','09/22/2016','1','2016-07-27 17:41:17','2016-07-27 17:41:17'),(22,'Mexico','Hot hot hot!!','09/29/2016','10/19/2016','3','2016-07-27 17:58:36','2016-07-27 17:58:36'),(23,'Canada','Cold is good','09/22/2016','10/21/2016','3','2016-07-27 18:00:22','2016-07-27 18:00:22'),(24,'Atlantic Ocean','I also like to float','01/19/2017','02/13/2017','3','2016-07-27 18:02:45','2016-07-27 18:02:45');
/*!40000 ALTER TABLE `trips` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `username` varchar(255) DEFAULT NULL,
  `pw_hash` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Test User','testuser','$2b$12$t5bYiUn4DUZjwvOIrBa.auIGRaR8wW/VDR9Pc.v6CKO5eopiI9U6y','2016-07-27 14:09:50','2016-07-27 14:09:50'),(2,'Charlie Brown','test','$2b$12$E3UwUtx5gC9LqGjIQhKepOuW0n.nSiXMFQjTT9piL9Y9YVOYWSDe6','2016-07-27 15:34:06','2016-07-27 15:34:06'),(3,'Sam','sammy','$2b$12$zAP4PYpOu5PCPti1K.6uX.kHWZezgWceGWqhcFifFR7Bi4FDJrPb.','2016-07-27 17:58:19','2016-07-27 17:58:19');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-27 18:12:30
