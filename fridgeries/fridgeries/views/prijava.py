from flask import Blueprint, render_template,request,Flask,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
import sqlite3

bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/prijava', methods=['GET','POST'])
def showprijava():
	if request.method == 'POST':
		if request.form.get('prij'):
			email = request.form.get('email')
			lozinka = request.form.get('lozinka')
			conn = sqlite3.connect('db/bazapodataka.db')
			curr = conn.cursor()
		
		emaildata = conn.execute("SELECT Email_Korisnika FROM Korisnik WHERE Email_Korisnika=?",(email,)).fetchone()
		lozinkadata = conn.execute("SELECT Lozinka_Korisnika FROM Korisnik WHERE Email_Korisnika=?",(email,)).fetchone()

		if emaildata is None:
			flash("Korisnik ne postoji")
			return render_template('prijava.html')
		else:	
			return redirect(url_for('fridgeries.views.naslovna.shownaslovna'))
					
	return render_template('prijava.html')
    