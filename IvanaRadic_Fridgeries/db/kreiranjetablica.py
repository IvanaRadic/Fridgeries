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
						
curr.execute("""CREATE TABLE Trenutno_u_Hladnjaku(
				Sokovi TEXT,
				Mlijecni_proizvodi TEXT,
				Povrce TEXT
							)""")
							
curr.execute("""CREATE TABLE Lista_za_Kupovinu(
				Sokovi TEXT,
				Mlijecni_proizvodi TEXT,
				Povrce TEXT
							)""")
				

conn.commit()
conn.close()
