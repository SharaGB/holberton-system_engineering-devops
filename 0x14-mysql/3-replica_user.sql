-- Create a new user for the replica server.
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY '';

-- replica_user must have the appropriate permissions to replicate your primary MySQL server.
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
