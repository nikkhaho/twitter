import psycopg2
def saveintb(tb,tag):

 try:
  conn = psycopg2.connect("dbname='dbtest' user='postgres' host='localhost' password='1375'")

 except:
  print ("I am unable to connect to the database.")

 cur = conn.cursor()

 cur.execute("INSERT INTO "+tb+" VALUES ( '"+tag+"')")
 conn.commit()
 conn.close()
 return "saved"
#-------------------------------------------------
def getfromtb(tb):

 try:
    conn = psycopg2.connect("dbname='dbtest' user='postgres' host='localhost' password='1375'")


 except:
  print ("I am unable to connect to the database.")

 cur = conn.cursor()
 try:
     cur.execute("""SELECT * from """ + tb)
 except:
    print ("I can't SELECT from bar")

 rows = cur.fetchall()
 return rows



