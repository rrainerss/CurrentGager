### CurrentGager - an essential tool for the money conscious electrical grid enjoyer.

To run CurrentGager on your Ubuntu machine, you must have:
- Python 3 installed
- Requests 2.22.0 library installed
- BeautifulSoup4 4.12.2 library installed

Install Python:
*sudo apt-get install python3.8*

Install Requests library:
*pip install requests==2.22.0*

Install BeautifulSoup library:
*pip install beautifulsoup4==4.12.2*
or
*sudo apt-get install python3-bs4=4.12.2*


pip install mysql-connector-python==8.0.32
sudo apt-get install python3-mysql.connector
sudo apt-get update  
sudo apt-get install mysql-server
sudo service mysql status
sudo service mysql restart
sudo mysql_secure_installation

<!-- sudo mysql -u root -->

<!-- USE mysql;
CREATE USER 'Rainers'@'localhost' IDENTIFIED BY '1432328770';
GRANT ALL PRIVILEGES ON *.* TO 'Rainers'@'localhost';
UPDATE user SET plugin='auth_socket' WHERE User='Rainers';
FLUSH PRIVILEGES;
sudo service mysql restart
sudo mysql -u Rainers
(these didnt work) -->


sudo mysql -u root -p
USE mysql;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '1432328770';
SELECT User, Host, plugin FROM mysql.user;

<!-- 
pip install alembic sqlalchemy
sudo apt install alembic
sudo apt install sqlalchemy
mkdir migrations
cd migrations
alembic init my_alembic
(then change the url)
alembic revision --autogenerate -m "Initial migration" -->

uncomment migrate line in main upon first run!!!!!!