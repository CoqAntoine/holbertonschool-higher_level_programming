-- Creates the table force_name
-- force_name description:
--      id INT
--      name VARCHAR(256) can’t be null

-- Create the table force_name if it does not already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
