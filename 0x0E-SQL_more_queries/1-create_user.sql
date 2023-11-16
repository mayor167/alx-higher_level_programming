-- Creates the user user_0d_1 with all privileges.
SELECT * FROM mysql.user WHERE User = 'user_0d_1';
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'%'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_0d_1'@'%'
   IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
