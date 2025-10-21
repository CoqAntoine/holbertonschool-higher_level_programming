-- Creates the database hbtn_0d_usa and the table cities
-- cities description:
--      id INT unique, auto generated, can’t be null and is a primary key
--      state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
--      name VARCHAR(256) can’t be null

-- Create the database if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the table cities if it does not already exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state FOREIGN KEY (state_id) REFERENCES states(id)
);
