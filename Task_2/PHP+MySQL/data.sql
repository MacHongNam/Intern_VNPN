-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 07, 2023 lúc 04:39 PM
-- Phiên bản máy phục vụ: 10.4.25-MariaDB
-- Phiên bản PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `task_2`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `task_2`
--

CREATE TABLE `task_2` (
  `id` int(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phonenumber` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `task_2`
--

INSERT INTO `task_2` (`id`, `username`, `password`, `address`, `phonenumber`) VALUES
(5, 'admin', 'c4ca4238a0b923820dcc509a6f75849b', 'Hà Đông - Hà Nội', '0345654678'),
(6, 'machongnam', '202cb962ac59075b964b07152d234b70', 'Đông Triều - Quảng Ninh', '0385908501'),
(7, 'test', '6512bd43d9caa6e02c990b0a82652dca', 'Hà Tây - Hà Nội', '0123456789'),
(8, 'buituananh', '81dc9bdb52d04dc20036dbd8313ed055', 'Thái Nguyên', '0454545454'),
(9, 'ttt', 'c4ca4238a0b923820dcc509a6f75849b', 'Hà Đông - Hà Nội', '0345654678'),
(10, 'zzz', '0cc175b9c0f1b6a831c399e269772661', 'Hà Đông - Hà Nội', '0345654678'),
(11, 'a', 'c4ca4238a0b923820dcc509a6f75849b', 'Hà Đông - Hà Nội', '0345654678'),
(12, 'nghiemtrunghau', 'e10adc3949ba59abbe56e057f20f883e', 'Hà Đông - Hà Nội', '08888888888'),
(13, 'hihihi', 'cfcd208495d565ef66e7dff9f98764da', 'Hải Phòng', '04545454545'),
(14, 'hasu', 'ffecb8a2f6cef0559940bd9542f3fa58', 'Hải Phòng', '11111111'),
(17, 'tranghasu', 'b3445aab49b2f5d287cc0e130a5da8df', 'Hải Phòng', '121212121'),
(18, 'yasuo', '4145a87ec0e7a641ccddff79ec42ee6d', 'Hà Đông - Hà Nội', '0385908501');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `task_2`
--
ALTER TABLE `task_2`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `task_2`
--
ALTER TABLE `task_2`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=173;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
