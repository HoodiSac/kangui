CREATE DATABASE  IF NOT EXISTS `stappenteller` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `stappenteller`;
-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: stappenteller
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `gebruiker`
--

DROP TABLE IF EXISTS `gebruiker`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gebruiker` (
  `id_user` int NOT NULL,
  `voornaam` varchar(45) DEFAULT NULL,
  `achternaam` varchar(45) DEFAULT NULL,
  `geslacht` varchar(3) DEFAULT NULL,
  `telefoonnummer` varchar(20) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `wachtwoord` varchar(45) NOT NULL,
  `stappen` int NOT NULL,
  `gezondheid` int NOT NULL,
  PRIMARY KEY (`id_user`),
  KEY `stappen` (`stappen`),
  KEY `gezondheid` (`gezondheid`),
  CONSTRAINT `gebruiker_ibfk_1` FOREIGN KEY (`stappen`) REFERENCES `stappen` (`id_stappen`),
  CONSTRAINT `gebruiker_ibfk_2` FOREIGN KEY (`gezondheid`) REFERENCES `gezondheid` (`id_gezondheid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gebruiker`
--

LOCK TABLES `gebruiker` WRITE;
/*!40000 ALTER TABLE `gebruiker` DISABLE KEYS */;
INSERT INTO `gebruiker` VALUES (1,'John','Doe','M','+123456789','john.doe@example.com','password123',1,1),(2,'Jane','Smith','F','+987654321','jane.smith@example.com','pass456',2,2),(3,'Bob','Johnson','M','+1122334455','bob.johnson@example.com','secure789',3,3),(4,'Alice','Williams','F','+9988776655','alice.williams@example.com','abc123',4,4),(5,'Charlie','Brown','M','+5544332211','charlie.brown@example.com','pwd567',5,5);
/*!40000 ALTER TABLE `gebruiker` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gezondheid`
--

DROP TABLE IF EXISTS `gezondheid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gezondheid` (
  `id_gezondheid` int NOT NULL,
  `lengte` float DEFAULT NULL,
  `gewicht` float DEFAULT NULL,
  `leeftijd` int DEFAULT NULL,
  `BPM` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id_gezondheid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gezondheid`
--

LOCK TABLES `gezondheid` WRITE;
/*!40000 ALTER TABLE `gezondheid` DISABLE KEYS */;
INSERT INTO `gezondheid` VALUES (1,175.5,70.2,30,'75'),(2,160,55.8,25,'82'),(3,185.2,80.5,35,'68'),(4,170.8,65,28,'80'),(5,155.3,52.1,22,'88');
/*!40000 ALTER TABLE `gezondheid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stappen`
--

DROP TABLE IF EXISTS `stappen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stappen` (
  `id_stappen` int NOT NULL,
  `stappen` int DEFAULT NULL,
  `doel` int DEFAULT NULL,
  `datum` timestamp(6) NOT NULL,
  PRIMARY KEY (`id_stappen`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stappen`
--

LOCK TABLES `stappen` WRITE;
/*!40000 ALTER TABLE `stappen` DISABLE KEYS */;
INSERT INTO `stappen` VALUES (1,8000,10000,'2023-01-01 07:00:00.000000'),(2,6000,8000,'2023-01-02 08:30:00.000000'),(3,10000,12000,'2023-01-03 11:45:00.000000'),(4,7500,9000,'2023-01-04 06:15:00.000000'),(5,9000,10000,'2023-01-05 09:00:00.000000');
/*!40000 ALTER TABLE `stappen` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-07 10:57:39
