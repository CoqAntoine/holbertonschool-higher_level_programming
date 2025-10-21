-- Creates the table unique_id
-- unique_id description:
--      id INT with the default value 1 and must be unique
--      name VARCHAR(256)

-- Create the table unique_id if it does not already exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
