-- Create a database named tyrell_corp
CREATE DATABASE IF NOT EXISTS tyrell_corp;

-- Within the tyrell_corp database create a table named nexus6 and add at least one entry to it.
CREATE TABLE IF NOT EXISTS tyrell_corp.nexus6 (id INT, name VARCHAR(256));
INSERT INTO `tyrell_corp.nexus6` (id, name) VALUES (1, 'Leon');

-- Make sure that holberton_user has SELECT permissions on your table so that we can check that the table exists and is not empty.
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
