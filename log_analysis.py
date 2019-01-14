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
