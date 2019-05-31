import sqlite3

conn = sqlite3.connect('bazapodataka.db')

curr = conn.cursor()

#Upis Korisnika#
curr.execute("INSERT INTO Korisnik VALUES ('Pero', 'Peric', 'lozinka123', 'pero@gmail.com')")
curr.execute("INSERT INTO Korisnik VALUES ('Ivo', 'Ivic', 'pas12345', 'ivoiv@hotmail.com')")
curr.execute("INSERT INTO Korisnik VALUES ('Marko', 'Maric', 'password142', 'markan@gmail.com')")

#Upis trenutnih namirnica u hladnjaku#
curr.execute("INSERT INTO Trenutno_u_Hladnjaku VALUES ('Sok od narance', 'mlijeko', 'rajcica')")
curr.execute("INSERT INTO Trenutno_u_Hladnjaku VALUES ('Coca Cola', 'sir', 'mrkva')")
curr.execute("INSERT INTO Trenutno_u_Hladnjaku VALUES ('', '', 'Kiseli krastavci')")

#Upis liste za kupovinu#
curr.execute("INSERT INTO Lista_za_Kupovinu VALUES ('Fanta', 'jogurt', 'Kupus')")
curr.execute("INSERT INTO Lista_za_Kupovinu VALUES ('Sprite', '', 'Zelena salata')")



conn.commit()
conn.close()
