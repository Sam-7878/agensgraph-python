import psycopg2
import agensgraph

conn = psycopg2.connect("dbname=test host=127.0.0.1 user=agens")
cur = conn.cursor()
cur.execute("DROP GRAPH IF EXISTS t CASCADE")
cur.execute("CREATE GRAPH t")
cur.execute("SET graph_path = t")

cur.execute("CREATE (:v {name: 'AgensGraph'})")
conn.commit();

cur.execute("MATCH (n) RETURN n")
v = cur.fetchone()[0]
print(v.props['name'])