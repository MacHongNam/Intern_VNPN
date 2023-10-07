CREATE DATABASE task_2

use task_2

CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    address NVARCHAR(255),
    phonenumber VARCHAR(20)
);

INSERT INTO users (username, password, address, phonenumber) VALUES 
('admin', 'c4ca4238a0b923820dcc509a6f75849b', N'Hà Đông - Hà Nội', '0345654678'),
('machongnam', '202cb962ac59075b964b07152d234b70', N'Đông Triều - Quảng Ninh', '0385908501'),
('test', '6512bd43d9caa6e02c990b0a82652dca', N'Hà Tây - Hà Nội', '0123456789'),
('buituananh', '81dc9bdb52d04dc20036dbd8313ed055', N'Thái Nguyên', '0454545454'),
('ttt', 'c4ca4238a0b923820dcc509a6f75849b', N'Hà Đông - Hà Nội', '0345654678'),
('zzz', '0cc175b9c0f1b6a831c399e269772661', N'Hà Đông - Hà Nội', '0345654678'),
('a', 'c4ca4238a0b923820dcc509a6f75849b', N'Hà Đông - Hà Nội', '0345654678'),
('nghiemtrunghau', 'e10adc3949ba59abbe56e057f20f883e', N'Hà Đông - Hà Nội', '08888888888'),
('hihihi', 'cfcd208495d565ef66e7dff9f98764da', N'Hải Phòng', '04545454545'),
('hasu', 'ffecb8a2f6cef0559940bd9542f3fa58', N'Hải Phòng', '11111111'),
('tranghasu', 'b3445aab49b2f5d287cc0e130a5da8df', N'Hải Phòng', '121212121'),
('yasuo', '4145a87ec0e7a641ccddff79ec42ee6d', N'Hà Đông - Hà Nội', '0385908501');
