import os


class CsvException(Exception):
    pass

class FichierIntrouvableException(CsvException):
    pass

class LigneInvalideException(CsvException):
    pass

class PrixNegatifException(CsvException):
    pass


def charger_csv(chemin):
    if not os.path.exists(chemin):
        raise FichierIntrouvableException(f"Fichier introuvable : {chemin}")

    articles = []

    with open(chemin, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.strip()

            if not ligne:
                continue  

            colonnes = ligne.split(";")

            if len(colonnes) != 3:
                raise LigneInvalideException(f"Ligne invalide : {ligne}")

            id_str, nom, prix_str = colonnes

            
            try:
                prix = float(prix_str)
            except ValueError:
                raise LigneInvalideException(f"Prix non numérique : {prix_str}")

            if prix < 0:
                raise PrixNegatifException(f"Prix négatif : {prix}")

            articles.append({
                "id": id_str,
                "nom": nom,
                "prix": prix
            })

    return articles
