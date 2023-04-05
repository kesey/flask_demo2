from flask import Flask
from flask import render_template
# from flask import url_for
from models import Destination, Bdd_interact
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name="home")

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', name="contacts")

@app.route('/panier')
def panier():
    return render_template('panier.html', name="panier")

@app.route('/destinations/<int:pays_id>')
def destinations(pays_id):
    bdd = Bdd_interact("xzhao_travel_bdd")
    bdd.create_table("destination", {"title": "TEXT", "price": "FLOAT", "duration": "TEXT", "resume": "TEXT", "include": "TEXT", "program": "TEXT"})
    destination = bdd.get_item(pays_id)
    match pays_id:
        case 1:
            return render_template('japon.html', infos_dest = destination)
        case 2:
            return render_template('chine.html', infos_dest = destination)
        case 3:
            return render_template('canada.html', infos_dest = destination)
        case _:
            return "error id"

if __name__== '__main__':
    app.run(debug=True)
    