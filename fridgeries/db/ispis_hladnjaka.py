#Ispis Podataka iz baze#

import sqlite3

#Spajanje na bazu#
conn = sqlite3.connect('bazapodataka.db')

curr = conn.cursor()


curr.execute('SELECT * FROM MojHladnjak')
for row in curr:
    print(row)

conn.commit()
conn.close()
