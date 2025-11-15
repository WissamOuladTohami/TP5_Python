import pytest

from csv_reader import (
    charger_csv,
    FichierIntrouvableException,
    LigneInvalideException,
    PrixNegatifException
)


def test_csv_valide(tmp_path):
    contenu = "1;Livre;25\n2;Stylo;3.5\n3;Table;100"
    fichier = tmp_path / "ok.csv"
    fichier.write_text(contenu)

    articles = charger_csv(str(fichier))
    assert len(articles) == 3


def test_fichier_absent():
    with pytest.raises(FichierIntrouvableException):
        charger_csv("introuvable.csv")


def test_prix_non_numerique(tmp_path):
    contenu = "1;Livre;abc"
    fichier = tmp_path / "bad.csv"
    fichier.write_text(contenu)

    with pytest.raises(LigneInvalideException):
        charger_csv(str(fichier))


def test_prix_negatif(tmp_path):
    contenu = "1;Livre;-5"
    fichier = tmp_path / "neg.csv"
    fichier.write_text(contenu)

    with pytest.raises(PrixNegatifException):
        charger_csv(str(fichier))
