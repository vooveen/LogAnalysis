import psycopg2

query1 = """SELECT title,count(*) AS sum
FROM log,articles
WHERE log.path=concat('/article/',articles.slug)
AND status = '200 OK'
GROUP BY articles.title
ORDER BY sum desc limit 3;
"""
query2 = """SELECT name,count(*) AS sum
FROM log,articles,authors
WHERE articles.author = authors.id
AND log.path=concat('/article/',articles.slug)
AND status = '200 OK'
GROUP BY name
ORDER BY sum desc;
"""
query3 = """SELECT to_char(time,'FMMonth DD,YYYY') AS date,
ROUND( AVG((status != '200 OK')::int * 100), 2) AS error_avg
FROM log
GROUP BY date
HAVING ROUND( AVG((status != '200 OK')::int * 100), 2)>1;
"""


def connect_db(query):
    try:
        # Connect to the database
        conn = psycopg2.connect("dbname=news")

        # Activate connection cursor
        cur = conn.cursor()
    except:
        print "Cannot connect to the database"
    # Execut the query
    cur.execute(query)
    # Fetch data
    return cur.fetchall()


def most_popular_articles(query):
    row = connect_db(query)
    print '\n+-------------------------------------------------------+'
    print "| What are the most popular three articles of all time? |"
    print '+-------------------------------------------------------+'
    for x in row:
        print '"'+x[0]+'" ---> '+str(x[1])+' views'


def most_popular_authors(query):
    row = connect_db(query)
    print '\n+-------------------------------------------------------+'
    print "| Who are the most popular article authors of all time? |"
    print '+-------------------------------------------------------+'
    for x in row:
        print '"'+x[0]+'" ---> '+str(x[1])+' views'


def days_requests_errors(query):
    row = connect_db(query)
    print '\n+------------------------------------------------------------+'
    print "| On which days did more than 1% of requests lead to errors? |"
    print '+------------------------------------------------------------+'
    for x in row:
        print ""+x[0]+' ---> '+str(x[1])+'%'+' errors\n'


most_popular_articles(query1)
most_popular_authors(query2)
days_requests_errors(query3)
