--prepares a MySQL server for the project
--database 'hbtnb_dev_db', new user'hbnb_dev'(in localhost)
--password for user set to 'hbtnb_dev_db'
-- grant all privileges to new user to db
-- grant select to databse 'performance_scheme'
-- script shouldn't fail if db or user exists

CREATE DATABASE IF NOT EXISTS `hbtnb_dev_db`;
CREATE USER IF NOT EXISTS `hbnb_dev`@`localhost` IDENTIFIED BY `hbnb_dev_pwd`;
GRANT ALL PRIVILEGES ON `hbtnb_dev_db`.* TO `hbnb_dev`@`localhost`;
GRANT SELECT ON `performance_schema`.* TO `hbnb_dev`@`localhost`;
