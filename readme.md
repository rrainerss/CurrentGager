### CurrentGager - an essential tool for the money conscious electrical grid enjoyer.

To run CurrentGager on your Ubuntu machine, you must have:
- Python 3.8 installed
- BeautifulSoup4 4.12.2 library installed
- MySQL 8.0.32 library installed
- PyTest 7.4.3 library installed
- PyTest mock 3.12.0 library installed

When you launch the program for the first time use *procedure.py*
All other times use *main.py*

Install Python:
*sudo apt-get install python3.8*

Install BeautifulSoup library:
*pip install beautifulsoup4==4.12.2*
or
*sudo apt-get install python3-bs4=4.12.2*

Install MySQL library:
*pip install mysql-connector-python==8.0.32*
or
*sudo apt-get install python3-mysql.connector*

Install PyTest library:
*pip install pytest==7.4.3*
or
*sudo apt-get install python3-pytest*
and
*pip install pytest pytest-mock==3.12.0*


Additional useful commands:
*sudo apt-get update*
*sudo apt-get install mysql-server*
*sudo service mysql status*
*sudo service mysql restart*
*sudo mysql_secure_installation*

*sudo mysql -u root -p*
*USE mysql;*
*ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '1432328770';*
*SELECT User, Host, plugin FROM mysql.user;*

*pip install pytest pytest-mock==3.12.0*
*pytest --cache-clear*
*pytest tests.py*

*chmod +x main.py*