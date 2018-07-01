Please NOTE:  This project was developed on a Windows 10 Laptop.
Due to a known bug in Windows 10, Hashicorp, makers of Vagrant has confirmed that there is a bug, but no bug fix.
It tool 6 months to find a solution since I had trouble getting support on this issue, which is why I am past due.
As a work around to this issue and not being able to run Vagrant and Virtual Box properly,
the project was developed using Postgresql and PgAdmin 4.
You will need to install and run Postgresql and PgAdmin4 on your computer.

copy this README.md and Newsdata.py files for this project in a directory under Downloads called News
where you should also have the newsdata.sql file found in the newsdata.zip file which will need to be extracted to the working News folder for the installed project.
Open your command prompt and switch to SSH and postgreSQL
change directory to downloads/News and in python run newsdata.py

The following files should be used for this project,  README.md, newsdata.py and newsdata.sql(found in newsdata.zip) file provided
from the Logs Analysis assignment

Access via the command line using psql command
log in with your postgres password
\l (to view the available databases, news should be one of the dbases set up.)
\c news (to switch to the news database)
news-# prompt should appear

# News

