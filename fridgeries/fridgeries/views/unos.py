from flask import Blueprint, render_template,request,Flask,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
import sqlite3

bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/unos', methods=['GET','POST'])
def showunos():
	if request.method == 'POST':
		if request.form.get('unos'):
			imenamirnice = request.form.get('imenamirnice')
			kategorija = request.form.get('kategorija')	
			if kategorija is None:
				return redirect(url_for('fridgeries.views.unos.showunos'))
			else:
				conn = sqlite3.connect('db/bazapodataka.db')
				curr = conn.cursor()
				conn.execute("insert into MojHladnjak (imenamirnice,kategorija) values(:imenamirnice,:kategorija)",
												{"imenamirnice":imenamirnice,"kategorija":kategorija})

				conn.commit()
			
				return redirect(url_for('fridgeries.views.naslovna.shownaslovna'))


	return render_template("unos.html")
    