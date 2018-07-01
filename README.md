Please NOTE:  This project was developed on a Windows 10 Laptop.
Due to a known bug in Windows 10, Hashicorp, makers of Vagrant has confirmed that there is a bug, but no bug fix.
It took me 6 months to find a working solution with the help of a mentor who uses Windows 10.
As a work around to this issue and not being able to run Vagrant and Virtual Box properly,
the project was developed using Postgresql and PgAdmin 4.
You will need to install and run Postgresql and PgAdmin4 on your computer.

copy this README.md and Newsdata.py files for this project in a directory under Downloads called News
where you should also have the newsdata.sql file for this project installed.
Open your command prompt and switch to SSH and postgreSQL
change directory to downloads/News and in python run newsdata.py

The following files should be used for this project,  README.md, newsdata.py and newsdata.sql (extracted from newsdata.zip) file provided
from the Logs Analysis assignment.  The newsdata.sql needed to be compressed in a .zip file to make the file size smaller to meet file size upload criteria.

Access via the command line using psql command
log in with your postgres password
\l (to view the available databases, news should be one of the dbases set up.)
\c news (to switch to the news database)
news-# prompt should appear

# News

