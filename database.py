import sqlite3

conn = sqlite3.connect("parc.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_prenom TEXT,
    matricule TEXT,
    service TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ordinateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type_ordinateur TEXT,
    nom_ordinateur TEXT,
    numero_serie TEXT,
    matricule TEXT
)
""")

conn.commit()
conn.close()

print("Base de données créée avec succès")