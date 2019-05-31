from flask import Blueprint, render_template


bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/registracija', methods=['POST','GET'])
def show():
		#if request.method == "POST":
		#ime = request.form.get("ime")
		#prezime = request.form.get("prezime")
		#email = request.form.get("email")
		#lozinka = request.form.get("lozinka")
		#secure_password = sha256_crypt.encrypt(str(lozinka))
		

   return render_template('registracija.html')