from flask import Blueprint, render_template,request,Flask,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
import sqlite3


bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/naslovna', methods=['POST','GET'])
def shownaslovna():	
	if request.method == 'POST':
		if request.form.get('prikaz'):
			conn = sqlite3.connect('db/bazapodataka.db')
			curr = conn.cursor()
			namirnice = curr.execute('SELECT * FROM MojHladnjak')
			result = curr.fetchall()
			for x in range(len(result)): 
				print (result[x]) 

	return render_template("naslovna.html")
    