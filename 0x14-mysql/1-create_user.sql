-- Create New MySQL User

-- Open a terminal window and launch the MySQL shell
sudo mysql -u root -p

CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

-- Give permissions to holberton_user so that we can check that the table exists and is not empty.
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- Exit the mysql terminal and execute the following command with password (projectcorrection280hbtn)
mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
