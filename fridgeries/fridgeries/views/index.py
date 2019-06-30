from flask import Blueprint, render_template, redirect, url_for


bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/')
def show():
   return redirect(url_for('fridgeries.views.prijava.showprijava'))