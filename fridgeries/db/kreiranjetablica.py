  #Kreiranje tablica#

import sqlite3

conn = sqlite3.connect('bazapodataka.db')

curr = conn.cursor()

curr.execute("""CREATE TABLE Korisnik (
           Ime_Korisnika TEXT NOT NULL,
           Prezime_Korisnika TEXT NOT NULL,
           Lozinka_Korisnika TEXT NOT NULL,
           Email_Korisnika TEXT NOT NULL,
		   PRIMARY KEY(Email_Korisnika)
						)""")
						
curr.execute("""CREATE TABLE MojHladnjak(
				imenamirnice TEXT NOT NULL
				kategorija TEXT NOT NULL
							)""")
							
				

conn.commit()
conn.close()
