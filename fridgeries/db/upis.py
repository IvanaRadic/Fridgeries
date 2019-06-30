import sqlite3

conn = sqlite3.connect('bazapodataka.db')

curr = conn.cursor()

#Upis Korisnika#
curr.execute("INSERT INTO Korisnik VALUES ('Pero', 'Peric', 'lozinka123', 'pero@gmail.com')")
curr.execute("INSERT INTO Korisnik VALUES ('Ivo', 'Ivic', 'pas12345', 'ivoiv@hotmail.com')")
curr.execute("INSERT INTO Korisnik VALUES ('Marko', 'Maric', 'password142', 'markan@gmail.com')")

#Upis trenutnih namirnica u hladnjaku#
curr.execute("INSERT INTO MojHladnjak VALUES ('Sok od narance', 'sokovi')")
curr.execute("INSERT INTO Trenutno_u_Hladnjaku VALUES ('Coca Cola', 'sokovi')")
curr.execute("INSERT INTO Trenutno_u_Hladnjaku VALUES ('Mlijeko', 'mlijecni_proizvodi')")
curr.execute("INSERT INTO Trenutno_u_Hladnjaku VALUES ('Sir', 'mlijecni_proizvodi')")
curr.execute("INSERT INTO Trenutno_u_Hladnjaku VALUES ('Kupus', 'povrce')")

conn.commit()
conn.close()
