CREATE DATABASE flight_data;
USE flight_data;
CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(50),
    departure DATETIME,
    arrival DATETIME,
    status VARCHAR(50)
);