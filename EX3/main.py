from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


def main():
    chemin = "articles.csv"

    try:
        articles = charger_csv(chemin)
        print("CSV importé avec succès.")
        for a in articles:
            print(a)

    except FichierIntrouvableException as e:
        print("Erreur :", e)

    except LigneInvalideException as e:
        print("Erreur de format CSV :", e)

    except PrixNegatifException as e:
        print("Erreur prix négatif :", e)

    except Exception as e:
        print("Erreur inattendue :", e)


if __name__ == "__main__":
    main()
