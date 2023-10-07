SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `task_2` (
    `id` int(255) NOT NULL
    `username` varchar(255) NOT NULL,
    `password` varchar(255) NOT NULL,
    `address` varchar(255),
    `phonenumber` varchar(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

INSERT INTO `users` (`username`,`password`,`address`,`phonenumber`) VALUES
('admin','c4ca4238a0b923820dcc509a6f75849b','Hà Đông - Hà Nội','0345654678'),
('machongnam','202cb962ac59075b964b07152d234b70','Đông Triều - Quảng Ninh','0385908501'),
('buituananh','81dc9bdb52d04dc20036dbd8313ed055','Thái Nguyên','0454545454')

ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `users`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
COMMIT;
