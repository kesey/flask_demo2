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
    bdd.delete_table("destination")
    bdd.create_table("destination", {"title": "TEXT", "price": "FLOAT", "duration": "TEXT", "resume": "TEXT", "include": "TEXT", "program": "TEXT"})
    dest1 = Destination("Japon", 800, "5 jours / 4 nuits", "Voyager au Japon, c'est une aventure unique et dépaysante. Vous découvrirez les trésors naturels et culturels du pays. Ces circuits que nous vous proposons vous permettront de découvrir toutes les facettes de l'archipel nippon. Les amateurs de nature et de randonnée seront ravis par les paysages montagneux, les bords de mer ou le mont Fuji. Les amoureux de la culture seront, eux, fascinés par les mégapoles comme Tokyo et leurs ambiances robotiques et technologiques mais aussi par leurs traditions ancestrales.", ("Vol A/R au départ de Paris(+10 autres villes)", "Demi-pension", "Chambre", "Transfert"), {"Jour 1": "France - Osaka", "Jour 2": "Osaka - Kobe - Himeji", "Jour 3": "Himeji - Hiroshima - Miyajima", "Jour 4": "Miyajima - Tokyo", "Jour 5": "Tokyo - France"}) 
    bdd.add_item("destination", dest1)
    dest2 = Destination("Chine", 1000, "5 jours / 4 nuits", "En Asie, venez découvrir la Chine ! Ce vaste pays vous charmera par sa culture, sa cuisine et ses paysages variés, entre grandes métropoles et petits villages de campagne. Les hôtels Kyriad vous accueillent à Pékin ou à Shanghai, à l’est du pays. Restaurant aux saveurs locales, literie de qualité et kiosque à magazines : nos hôtels ont tout bon !", ("Vol A/R au départ de Paris(+10 autres villes)", "Demi-pension", "Chambre", "Transfert"), {"Jour 1": "France - Pékin", "Jour 2": "Pékin - Xian", "Jour 3": "Xian - Wuhan - Shanghai", "Jour 4": "Shanghai - Hangzhou - Xiamen", "Jour 5": "Ximen - France"}) 
    bdd.add_item("destination", dest2)
    dest3 = Destination("Canada", 600, "5 jours / 4 nuits", "Réservez votre séjour ou circuit pas cher au Canada et explorez le Grand Nord à travers l’immensité des grands espaces du Canada. En choisissant nos séjours au Canada, vous découvrirez ce vaste pays à la culture et à la nature très riche. Balade en chiens de traîneau, randonnée dans des forêts s’étendant sur des hectares, des lacs à admirer par milliers, la nature occupe une place primordiale au Canada. Du blanc enneigé à perte de vue en hiver jusqu’aux fleurs colorées des flancs de montagne en été en passant par le vert des paysages du printemps, les amateurs de nature et de grands espaces seront au paradis ! Parmis nos offres, optez pour un séjour à Montréal pour découvrir la plus grande ville du Québec ! Réservez un voyage à Toronto pour visiter cette métropole dynamique et pourquoi pas faire un détour vers les chutes du Niagara. Partez en séjour à Québec et explorez son architecture colonial sans pareil en longeant le fleuve Saint-Laurent. Découvrez nos conseils et informations pratiques pour préparer votre voyage au Canada.", ("Vol A/R au départ de Paris(+10 autres villes)", "Demi-pension", "Chambre", "Transfert"), {"Jour 1": "France - Vancouver", "Jour 2": "Vancouver - Victoria", "Jour 3": "Victoria - Pacific Rim - Whistler", "Jour 4": "Whistler - Parc Wells Gray - Jasper", "Jour 5": "Jasper - France"}) 
    bdd.add_item("destination", dest3)
    all_items = bdd.get_all_items("destination")
    print(all_items)
    destination = bdd.get_item("destination", pays_id)
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
    