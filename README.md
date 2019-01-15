# Logs Analysis

## About

This is a python program to extract information from a newspaper site database

## Requirements

Python 2.x.x You can download it from the official site [Pyhton](https://www.python.org/downloads/)
psycopg2 Here is instructions to download it [psycopg2](http://initd.org/psycopg/download/)

## Design of the code

1-In this program i used psycopg2 library to connect to the psql database.
2-i've created connect_db() function it connects to the database, fetchs data
from it and returns it.
3-i've created 3 functions :
    1-most_popular_articles()
    2-most_popular_authors()
    3-days_requests_errors()
they take what the connect_db() function return and print it

## How to run this program 

1-Download the zip file or clone the repository.
2-Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3-Unzip the downloaded files.
4-Open your Terminal.
5-cd to the database file directory.
6-To create the database run the following command line :
    psql -d news -f newsdata.sql
psql : the PostgreSQL command line program
-d news : connect to the database named news (the database should have this name to avoid problems running the program)
-f newsdata.sql : run the SQL statements in the file newsdata.sql
7-cd to program file's "log_analysis.py" directory 
8-At the end run the following command line to run the program :
    python log_analysis.py