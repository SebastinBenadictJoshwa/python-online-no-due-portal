-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307
-- Generation Time: Mar 26, 2023 at 06:15 AM
-- Server version: 10.1.29-MariaDB
-- PHP Version: 7.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `1collegeasspy`
--

-- --------------------------------------------------------

--
-- Table structure for table `noduetb`
--

CREATE TABLE `noduetb` (
  `id` int(11) NOT NULL,
  `regno` varchar(255) DEFAULT NULL,
  `department` varchar(255) DEFAULT NULL,
  `year` varchar(255) DEFAULT NULL,
  `request_date` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `noduetb`
--

INSERT INTO `noduetb` (`id`, `regno`, `department`, `year`, `request_date`, `status`) VALUES
(1, '20ubc609', 'BCA', 'III', '2023-03-25', 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `Regno` varchar(250) NOT NULL,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Age` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Phone` varchar(250) NOT NULL,
  `Address` varchar(250) NOT NULL,
  `Degree` varchar(250) NOT NULL,
  `Department` varchar(250) NOT NULL,
  `Year` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`Regno`, `Name`, `Gender`, `Age`, `Email`, `Phone`, `Address`, `Degree`, `Department`, `Year`) VALUES
('20UBC609', 'Sebastin Benadict Joshwa D', 'male', '20', 'joshwadsb@gmail.com', '8883166011', 'No. 438, Valayampatti, Sivagangai   District', 'bca', 'it', '3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `noduetb`
--
ALTER TABLE `noduetb`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `noduetb`
--
ALTER TABLE `noduetb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
