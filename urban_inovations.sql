-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 03, 2024 at 11:00 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `urban_inovations`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_details`
--

CREATE TABLE `account_details` (
  `sno` int(11) NOT NULL,
  `email` text NOT NULL,
  `phone_no` int(11) NOT NULL,
  `address` text NOT NULL,
  `name` text NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account_details`
--

INSERT INTO `account_details` (`sno`, `email`, `phone_no`, `address`, `name`, `date`) VALUES
(1, 'vina21ec@cmrit.ac.in', 888468198, '186, 5TH FLOOR, 3RD CROSS', 'vinay', '2024-03-03 09:44:12'),
(2, 'rajeshvinay186@gmail.com', 888468198, '186, 5TH FLOOR, 3RD CROSS', 'gopal', '2024-03-03 09:54:41'),
(3, 'vinaygopal2410@gmail.com', 2147483647, '186, 5TH FLOOR, 3RD CROSS', 'suhani', '2024-03-03 09:56:05');

-- --------------------------------------------------------

--
-- Table structure for table `booking_details`
--

CREATE TABLE `booking_details` (
  `count` int(11) NOT NULL,
  `sno` int(11) NOT NULL,
  `cost` int(11) NOT NULL,
  `transaction_id` text NOT NULL,
  `email` text NOT NULL,
  `date_of_booking` datetime NOT NULL,
  `type` text NOT NULL,
  `name` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `booking_details`
--

INSERT INTO `booking_details` (`count`, `sno`, `cost`, `transaction_id`, `email`, `date_of_booking`, `type`, `name`) VALUES
(1, 1, 10000, '836550020426', 'vina21ec@cmrit.ac.in', '2024-03-31 00:00:00', 'Kitchen', 'vinay'),
(2, 3, 50000, '520106161851', 'vinaygopal2410@gmail.com', '2024-04-14 00:00:00', 'Bedroom', 'suhani'),
(3, 3, 50000, '163826487460', 'vinaygopal2410@gmail.com', '2024-04-14 00:00:00', 'Bedroom', 'suhani');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `sno` int(11) NOT NULL,
  `email` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`sno`, `email`, `password`) VALUES
(1, 'vina21ec@cmrit.ac.in', 'z679lrsuqxy1djkm289#'),
(2, 'rajeshvinay186@gmail.com', 'jpqsryz2sz13djkmouvy'),
(3, 'vinaygopal2410@gmail.com', 'v346y568kqrtdjkmqxy1lrsu');

-- --------------------------------------------------------

--
-- Table structure for table `payment_details`
--

CREATE TABLE `payment_details` (
  `count` int(11) NOT NULL,
  `sno` int(11) NOT NULL,
  `card_number` text NOT NULL,
  `card_holder` text NOT NULL,
  `cost` int(11) NOT NULL,
  `transaction_id` text NOT NULL,
  `expiry_date` text NOT NULL,
  `cvv` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payment_details`
--

INSERT INTO `payment_details` (`count`, `sno`, `card_number`, `card_holder`, `cost`, `transaction_id`, `expiry_date`, `cvv`) VALUES
(1, 1, '2342 3424 2232 4454', 'gopal', 10000, '836550020426', '23/42', 423),
(2, 3, '7879 4964 6966 2326', 'suhani', 50000, '520106161851', '12/25', 265),
(3, 3, '7879 4964 6966 2326', 'suhani', 50000, '163826487460', '12/25', 265);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_details`
--
ALTER TABLE `account_details`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `booking_details`
--
ALTER TABLE `booking_details`
  ADD PRIMARY KEY (`count`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `payment_details`
--
ALTER TABLE `payment_details`
  ADD PRIMARY KEY (`count`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account_details`
--
ALTER TABLE `account_details`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `booking_details`
--
ALTER TABLE `booking_details`
  MODIFY `count` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `payment_details`
--
ALTER TABLE `payment_details`
  MODIFY `count` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
