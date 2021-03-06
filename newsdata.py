#This script will run 3 seperate queries from the News DB and it's 3 seperate
#tables, called
#articles, authors and log
#This script assumes that you will be running the python script in
#SSH from postgreSQL.
#Make sure your Newsdata SQL files are setup and installed in postgreSQL.
#

import psycopg2

# Connect to an existing database
conn = psycopg2.connect(
        "host='localhost' dbname='news' user='postgres' password='postgres'")


# Open a cursor to perform database operations
cur = conn.cursor()

#New Command, Executes and prints out results of question 1 in Logs
#Analysis project.
cur.execute(
    "SELECT articles.title AS Articles_Name,"
    "COUNT (log.time) AS Views "
    "FROM articles, log "
    "WHERE substring(log.path,10) = articles.slug "
    "GROUP BY articles.title "
    "ORDER BY Views DESC LIMIT 3 "
          )
results = cur.fetchall()

print ("QUERY 1 - Popular Articles")
for item in results:
    print("{} - {} Views".format(item[0], item[1]))
print("--------------------------------------------")

#New Command, Executes and prints out results of question 2 for Authors
#Views in Analysis project.
cur.execute(
    "SELECT authors.name AS Authors_Name, COUNT (log.time) AS Views "
    "FROM authors, articles, log "
    "WHERE articles.author = authors.id "
    "GROUP BY authors.name "
    "ORDER BY Views DESC "
)
results = cur.fetchall()

print ("QUERY 2 - Authors Views")
for item in results:
      print("{} - {:,} Views".format(item[0], item[1]))
print("--------------------------------------------")

#New Command, Executes and prints out results of question 3 in Logs
#Analysis project showing days where log errors greater than 1%.
cur.execute (
    "SELECT * "
    "FROM ( "
    "SELECT to_char(time,'MonthDD, YYYY') as date,"
    "(COUNT(status) filter "
    "(WHERE status LIKE '404%')*100.0/COUNT(status))"
    "as errors "
    "FROM log "
    "GROUP BY date) as errors_table "
    "WHERE errors_table.errors > 1.0 "
)

results = cur.fetchall()

print ("QUERY 3 - Days Errors > 1%")
for item in results:
     print("{} - {} Views".format(item[0], item[1]))
print("--------------------------------------------")

conn.close()
