--prepares MySQL server with database `hbnb_test_db`
--new user `hbnb_test` in localhost with password `hbnb_test_db`
--user should have all privileges on db
-- user should have SELECT privilege on database `performance_schema`
--script should not fail if db or user exists

CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
CREATE USER IF NOT EXISTS `hbnb_test`@`localhost` IDENTIFIED BY `hbnb_test_pwd`;
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO `hbnb_test`@`localhost`;
GRANT SELECT ON `performance_schema`.* TO `hbnb_test`@`localhost`;
