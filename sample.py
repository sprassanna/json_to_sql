import psycopg2

conn = psycopg2.connect(
    database="xerxes-dev",
    user="xerxes",
    host="localhost",
    port="5432"
)

cur = conn.cursor();

cur.execute("INSERT INTO users(email, username, first_name, last_name, display_name)values('ssekar802@apac.comcast.com', 'ssekar802', 'Saravanan', 'Sekar', 'Saro')");

conn.commit()

cur.execute("SELECT * from users")
rows = cur.fetchall();

for row in rows:
    print('email :' ,row[0])
    print('username :' ,row[1])

print("INSERT query executed")
conn.close()