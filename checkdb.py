import psycopg2
def checkindb(tb,value,clone):

   try:
    conn = psycopg2.connect("dbname='dbtest' user='postgres' host='localhost' password='1375'")


   except:
     print ("I am unable to connect to the database.")

   cur = conn.cursor()
   try:
      cur.execute("""SELECT * from """+tb+"""  WHERE  """+clone+"""='"""+value+"""'""")
   except:
    print ("I can't SELECT from bar")

   rows = cur.fetchall()
   if rows:h="ok"
   else:h="no"

   return h
   conn.commit()
   conn.close()
