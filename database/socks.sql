-- phpMyAdmin SQL Dump
-- version 4.5.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 09, 2017 at 08:24 PM
-- Server version: 10.1.19-MariaDB
-- PHP Version: 5.6.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sockmarket`
--

-- --------------------------------------------------------

--
-- Table structure for table `socks`
--

CREATE TABLE `socks` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `style` text NOT NULL,
  `color` text NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(16,2) NOT NULL,
  `updated` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `socks`
--

INSERT INTO `socks` (`id`, `name`, `style`, `color`, `quantity`, `price`, `updated`) VALUES
(1, 'Suzanne', 'knee-high', 'red', 18, '4.99', '01-22-2016'),
(2, 'Marianne', 'ankle', 'blue stripe', 30, '3.50', '01-23-2016'),
(3, 'Jenny', 'mini', 'blue', 10, '3.45', '01-13-2016'),
(4, 'O\\''Shannon', 'knee-high', 'green', 24, '2.99', '01-23-2016'),
(5, 'Daphne', 'knee-high', 'pink', 6, '6.25', '01-22-2016'),
(7, 'Luanne', 'ankle', 'pink', 3, '0.00', '01-22-2016'),
(8, 'Nancie', 'mini', 'purple', 10, '4.25', '01-13-2016'),
(10, 'Olivia', 'ankle', 'gray', 12, '2.95', '01-13-2016'),
(11, 'Queen Anne', 'knee-high', 'yellow', 12, '4.99', '01-13-2016'),
(12, 'Rhiann', 'mini', 'pink', 36, '3.99', '01-13-2016'),
(15, 'D\\''Shawn', 'mini', 'blue', 24, '2.99', '01-23-2016'),
(16, 'Abigail', 'ankle', 'blue', 24, '1.99', '01-22-2016'),
(18, 'Greta', 'ankle', 'blue', 12, '6.25', '01-14-2016'),
(19, 'Hermione', 'knee-high', 'argyle/multi', 12, '5.99', '01-22-2016'),
(20, 'Isabel', 'mini', 'white', 30, '1.99', '01-14-2016'),
(21, 'Kylie', 'ankle', 'green', 24, '2.25', '01-14-2016'),
(22, 'Lulu', 'ankle', 'polka-dot/multi', 12, '2.99', '01-14-2016'),
(23, 'Michelle', 'ankle', 'pink', 12, '1.99', '01-14-2016'),
(24, 'Susy', 'other', 'black stripe', 12, '3.50', '01-22-2016'),
(25, 'Tanya', 'mini', 'red', 12, '4.00', '01-22-2016'),
(26, 'Ursula', 'knee-high', 'purple', 6, '3.99', '01-14-2016'),
(27, 'Theresa', 'other', 'brown', 12, '1.99', '01-23-2016'),
(28, 'Vivien', 'knee-high', 'red', 12, '3.00', '01-14-2016'),
(29, 'Lucia', 'knee-high', 'yellow', 18, '1.25', '01-14-2016'),
(30, 'Princess Anne', 'knee-high', 'pink', 24, '4.25', '01-22-2016'),
(32, 'Faith', 'knee-high', 'black polka-dot', 12, '3.99', '01-22-2016'),
(33, 'Fatima', 'knee-high', 'black stripe', 12, '4.99', '01-14-2016'),
(35, 'Fay', 'ankle', 'pink', 12, '3.00', '01-14-2016'),
(39, 'Steffie', 'knee-high', 'dark purple', 12, '4.00', '01-23-2016'),
(40, 'Lizzy', 'mini', 'red', 12, '2.75', '01-15-2016'),
(41, 'Denise', 'knee-high', 'red', 36, '2.25', '01-15-2016'),
(43, 'Alex', 'knee-high', 'blue', 12, '3.99', '01-16-2016'),
(44, 'Evelyn', 'knee-high', 'black multi', 24, '3.50', '01-18-2016'),
(46, 'Diane', 'ankle', 'yellow', 12, '2.99', '01-22-2016'),
(48, 'Volta', 'ankle', 'pink multi', 36, '4.99', '01-21-2016'),
(49, 'Wendy', 'knee-high', 'argyle', 12, '6.99', '01-22-2016'),
(50, 'Alice', 'knee-high', 'pink', 24, '2.49', '01-22-2016'),
(52, 'Faye', 'mini', 'dark purple', 24, '1.99', '01-21-2016'),
(53, 'Victoria', 'knee-high', 'striped multi', 12, '1.99', '01-22-2016'),
(54, 'Viva', 'knee-high', 'striped multi', 36, '1.99', '01-22-2016'),
(55, 'Terrie', 'mini', 'blue stripe', 12, '3.99', '01-23-2016'),
(56, 'Charlie', 'knee-high', 'argyle - blue/red', 12, '3.50', '01-22-2016'),
(58, 'Jo-Anne', 'mini', 'brown', 12, '3.49', '01-22-2016'),
(59, 'Ilsa', 'ankle', 'orange', 12, '2.45', '01-23-2016'),
(60, 'Bonnie', 'knee-high', 'argyle', 12, '3.99', '01-23-2016'),
(61, 'Maryann', 'ankle', 'white', 12, '3.49', '01-23-2016'),
(62, 'Krissie', 'mini', 'blue', 12, '1.99', '01-23-2016'),
(63, 'Izzy', 'ankle', 'blue and white', 36, '2.99', '01-23-2016'),
(64, 'Izzy', 'ankle', 'brown and white', 12, '2.99', '01-23-2016'),
(65, 'Alberta', 'knee-high', 'orange and blue', 36, '4.99', '01-23-2016'),
(66, 'Nicole', 'knee-high', 'pink', 6, '10.99', '01-31-2017'),
(67, 'Caitlin', 'knee-high', 'pink', 8, '12.99', '01-31-2017'),
(68, 'Victoria', 'ankle', 'pink', 6, '1.99', '01-31-2017');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `socks`
--
ALTER TABLE `socks`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `socks`
--
ALTER TABLE `socks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
