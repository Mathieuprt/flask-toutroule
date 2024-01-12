import sqlite3
import os

def f_createDB():

    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(base_dir, 'enquete.db')

    if os.path.isfile(db_path):
        print("La base existe déjà")
    else: 
        connexion = sqlite3.connect(db_path)
        curseur = connexion.cursor()
        curseur.execute('''
            CREATE TABLE IF NOT EXISTS enquete (
                id INTEGER PRIMARY KEY NOT NULL,
                nom TEXT NOT NULL,
                prenom TEXT NOT NULL,
                civilite TEXT NOT NULL,
                typeVehicule TEXT NOT NULL,
                nbKm FLOAT NOT NULL,
                commentaire TEXT NULL
            );''')
        connexion.commit()
        connexion.close()
    return db_path
            