-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 22, 2021 at 06:22 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `food`
--

-- --------------------------------------------------------

--
-- Table structure for table `food_team`
--

CREATE TABLE `food_team` (
  `food_it` varchar(30) NOT NULL,
  `klr` int(11) NOT NULL,
  `pro` int(11) NOT NULL,
  `co` int(11) NOT NULL,
  `fat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `food_team`
--

INSERT INTO `food_team` (`food_it`, `klr`, `pro`, `co`, `fat`) VALUES
('Chicken ', 300, 180, 12, 100),
('Chicken_Briyani', 290, 20, 31, 9),
('Egg', 78, 6, 1, 5),
('idly', 39, 3, 30, 8),
('Maida_Bread', 265, 9, 200, 49),
('Rice', 194, 5, 120, 1),
('Wheat_Bread', 67, 2, 13, 45);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `food_team`
--
ALTER TABLE `food_team`
  ADD PRIMARY KEY (`food_it`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
