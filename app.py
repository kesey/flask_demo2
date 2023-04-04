from flask import Flask
from flask import render_template
from flask import url_for
# from models import Destination
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
    match pays_id:
        case 1:
            return render_template('Japon.html', name="japon")
        case 2:
            return render_template('Chine.html', name="chine")
        case 3:
            return render_template('Canada.html', name="canada")
        case _:
            return "error id"

if __name__== '__main__':
    app.run(debug=True)
    