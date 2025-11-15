# Exercice 1 – Gestion des erreurs en Python
---

### Objectif pédagogique

Comprendre la gestion des erreurs en Python, notamment la définition et l'utilisation de ses propres exceptions pour capturer des cas métiers spécifiques.

---

### Description

- **Exception personnalisée** : `SoldeInsuffisantException` pour signaler un retrait supérieur au solde disponible.  
- **Classe CompteBancaire** : contient les attributs `nom` et `solde`.  
- **Méthodes** : 
  - `deposer(montant)` : ajoute un montant au solde si positif.  
  - `retirer(montant)` : retire un montant si suffisant, sinon lève `SoldeInsuffisantException`.  
  - `afficher()` : affiche le nom du compte et le solde.  
- **Gestion des erreurs** : les exceptions sont capturées dans un bloc `try/except` pour un affichage utilisateur clair.

---

### Exemple d’utilisation

- Créer un compte bancaire pour "Alice" avec un solde initial de 100€  
- Afficher le solde  
- Tenter de retirer 150€ et gérer l’exception si le solde est insuffisant

---

### Résultat attendu

<img width="1412" height="327" alt="EX1" src="https://github.com/user-attachments/assets/d2ff168e-71df-4b6b-b7d0-16fb16e04ff1" />

---

# Exercice 2 – Gestion des réservations et exceptions métier
---

### Objectif pédagogique

Apprendre à concevoir un système robuste en définissant plusieurs types d’exceptions spécifiques à un domaine métier, tout en appliquant de bonnes pratiques de validation et de journalisation.

---

### Description

- **Exceptions personnalisées** : 
  - `ReservationException` (classe de base)
  - `CapaciteDepasseeException`
  - `NombreInvalideException`
  - `NomClientInvalideException`  
- **Classe métier** : `Evenement` avec les attributs :
  - `nom` (str)  
  - `capacite` (int)  
  - `places_reservees` (int)  
- **Méthodes** :
  - `reserver(nom_client, nb_places)` : vérifie la validité du client et du nombre de places, lève les exceptions si nécessaire, sinon confirme la réservation.  
  - `afficher()` : affiche l’état actuel des réservations.  

---

### Exemple d’utilisation

- Créer un événement "Concert" avec 5 places disponibles  
- Tenter de réserver 2 places avec un nom de client vide  
- Capturer et afficher l’exception générée

---

### Résultat attendu

<img width="1410" height="402" alt="EX2" src="https://github.com/user-attachments/assets/9e7fa886-babe-438b-9330-ed05e084cf68" />

---

# Exercice 3 – Import CSV sécurisé avec exceptions personnalisées
---

### Objectif pédagogique

Renforcer la maîtrise des exceptions personnalisées appliquées à la lecture et à la validation de fichiers CSV, en séparant clairement le flux nominal et les erreurs métier.

---

### Description

- **Scénario** : lire un fichier CSV d’articles (`id;nom;prix`) et vérifier :  
  - l’existence du fichier  
  - le format de chaque ligne  
  - la validité du prix (numérique et positif)  

- **Hiérarchie des exceptions** :  
  - `CsvException` (classe de base)  
    - `FichierIntrouvableException`  
    - `LigneInvalideException`  
    - `PrixNegatifException`  

- **Fonctionnalités clés** :  
  - `charger_csv(chemin)` : retourne une liste de dictionnaires ou lève une exception appropriée  
  - Gestion des exceptions dans `main.py` pour afficher des messages clairs à l’utilisateur  
  - Logger facultatif pour tracer les anomalies dans `erreurs.log`  

- **Contraintes** :  
  - Ne pas utiliser `print` pour la logique métier, lever des exceptions à la place  
  - Ignorer les lignes vides  
  - Valider que le prix est convertible en float et supérieur à 0  

---

### Exemple d’utilisation

- Tenter de charger un fichier CSV  
- Capturer les exceptions possibles pour afficher un message utilisateur clair  
- Ignorer les lignes vides et les anomalies de prix ou de format

---

### Résultat attendu 

<img width="1412" height="302" alt="EX3" src="https://github.com/user-attachments/assets/39450222-a30b-4e7e-b027-b00a716c29fe" />




