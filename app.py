from flask import Flask, render_template, request
from dotenv import load_dotenv
from database.bdd import f_createDB
import sqlite3

load_dotenv()

app = Flask(__name__)

# Ligne du dessous à ne garder qu'en mode de développement
app.config["CACHE_TYPE"] = "null"

# Appel à f_createDB pour créer la base de données au démarrage de l'application
db_path = f_createDB()

@app.route("/")
# f_ : route pour Flask
def f_index():
    return render_template("index.html")

@app.route('/formulaire', methods=['GET', 'POST'])
def f_formulaire():
   if request.method == 'POST':
       f_nom = request.form.get('nom')
       f_prenom = request.form.get('prenom')
       f_civilite = request.form.get('civilite')
       f_typevehicule = request.form.get('typeVehicule')
       f_nbKm = request.form.get('nbKm')
       f_commentaire = request.form.get('commentaire')

       # J'enregistre tout ça dans ma database
       connexion = sqlite3.connect(db_path)
       curseur = connexion.cursor()
       curseur.execute('''
            INSERT INTO enquete (nom, prenom, civilite, typeVehicule, nbKm, commentaire) 
            VALUES (?, ?, ?, ?, ?, ?)''',
            (f_nom, f_prenom, f_civilite, f_typevehicule, f_nbKm, f_commentaire))
       connexion.commit()
       connexion.close()
       
       return render_template("form.html",
                                t_nom = f_nom,
                                t_prenom = f_prenom,
                                t_civilite = f_civilite,
                                t_typevehicule = f_typevehicule,
                                t_nbKm = f_nbKm,
                                t_commentaire = f_commentaire)
   return render_template("form.html")


#Route vers la page du dashboard
@app.route('/dashboard')
def f_dashboard(): 
    return render_template('dashboard.html')

#Route vers la page de contact
@app.route('/contact')
def f_contact(): 
    return render_template('contact.html')