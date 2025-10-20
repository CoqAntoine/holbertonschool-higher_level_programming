-- Script that creates a table called first_table in the database
-- The table should have:
--      id INT
--      name VARCHAR(256)
-- Does not fail if the table already exists

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
