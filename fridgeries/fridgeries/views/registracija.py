from flask import Blueprint, render_template,request,Flask,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
import sqlite3

bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/registracija', methods=['POST','GET'])
def showregistracija():
	if request.method == 'POST':
		if request.form.get('reg'):
			ime = request.form.get('ime')
			prezime = request.form.get('prezime')
			email = request.form.get('email')
			lozinka = request.form.get('lozinka')
			conn = sqlite3.connect('db/bazapodataka.db')
			curr = conn.cursor()
			emaildata = conn.execute("SELECT Email_Korisnika FROM Korisnik WHERE Email_Korisnika=?",(email,)).fetchone()
			if emaildata is None:
				conn.execute("INSERT into Korisnik (Ime_Korisnika,Prezime_Korisnika,Email_Korisnika,Lozinka_Korisnika) VALUES(:ime,:prezime,:email,:lozinka)",
													{"ime":ime,"prezime":prezime,"email":email,"lozinka":lozinka})
				conn.commit()
				flash("Uspjesno ste se registrirali, prijavite se!")
				return redirect(url_for('fridgeries.views.prijava.showprijava'))
			else:
				flash("Korisnik već postoji")
				return render_template('registracija.html')
			

	return render_template('registracija.html')