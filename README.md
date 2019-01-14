# Logs Analysis

## About
This is a python program to extract information from a newspaper site database

## Requirements
Python 2.x.x

## Design of the code
1.In this program i used psycopg2 library to connect to the psql database.
2.i've created connect_db() function it connects to the database, fetchs data
from it and returns it.
3.i've created 3 functions :
    1.most_popular_articles()
    2.most_popular_authors()
    3.days_requests_errors()
they take what the connect_db() function returns and print it

## How to run this program 
1.Download the zip file or clone the repository.
2.Unzip the file.
3.Open your Terminal.
4.cd the file directory.
5.Run this command line :
  python log_analysis.py