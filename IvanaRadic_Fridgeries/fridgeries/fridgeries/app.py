from flask import Flask
from passlib.hash import sha256_crypt
from fridgeries.views.index import bp as index_bp
from fridgeries.views.registracija import bp as registracija_bp
from fridgeries.views.prijava import bp as prijava_bp


app = Flask(__name__)


app.register_blueprint(index_bp)
app.register_blueprint(registracija_bp)
app.register_blueprint(prijava_bp)


