import sqlite3 as sql
db=sql.connect("db.db")
cursor=db.cursor()
#cursor.execute("""CREATE TABLE Place (num INTEGER(5) PRIMARY KEY,etat CHAR(1) CHECk(etat in ('O','l')),prix INTEGER(8) DEFAULT 0)""")

#cursor.execute ("""INSERT INTO Place VALUES (10,"O",0)""")
cursor.execute ("INSERT INTO Place VALUES (11,'O',0)")
cursor.execute ("""INSERT INTO Place VALUES (13,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (14,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (15,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (16,"O",0)""")

cursor.execute ("""INSERT INTO Place VALUES (20,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (21,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (23,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (24,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (25,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (26,"O",0)""")

cursor.execute ("""INSERT INTO Place VALUES (30,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (31,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (33,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (34,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (35,"O",0)""")
cursor.execute ("""INSERT INTO Place VALUES (36,"O",0)""")

