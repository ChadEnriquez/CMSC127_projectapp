# Expense Tracker
## CMSC 127 S3L PROJECT 

### Group 3 - S3L Members: 
	- Chad Andrei A. Enriquez
	- Genevieve D. Penes
	- Ryan G. Villacorte

### Requirements (Windows):
	
	1. At least Python version 3.11.3 (latest version as of making this project) 
    	- Download here:
		- https://www.python.org/downloads/

		- if you already have Python installed, check if you have PIP installed
		- use the commands below on a command terminal to install PIP
		- curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
		- python get-pip.py
		- pip --version 
	
	2. MySQL Connector for Python 
		- Download here:
		- https://dev.mysql.com/downloads/connector/python/
		- or
		- use the command below on a command terminal to install MySQL Connector for Python
		- pip install mysql-connector-python
  
	3. MariaDB
    	- Download here:
    	- https://mariadb.com/downloads/
  
### Instructions for running:
	1. from the root terminal (MariaDB), use the command below to setup the database
    	- CREATE USER 'user'@localhost IDENTIFIED BY 'pass';
    	- GRANT ALL PRIVILEGES ON *.* TO 'user'@'localhost';
	2. 

### References used:
	- https://www.youtube.com/watch?v=oDR7k66x-AU&ab_channel=DiscoverPython
  	- https://www.w3schools.com/python/python_mysql_getstarted.asp
