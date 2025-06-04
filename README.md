# Aplicație Web – Baza de Date Studenți
# Ion Robert Florin
Acest proiect reprezintă o aplicație web complet funcțională, realizată ca **lucrare de licență** în cadrul **Facultății de Informatică – Universitatea Titu Maiorescu**.

Scopul aplicației este de a oferi un sistem simplu și eficient pentru **gestionarea informațiilor academice ale studenților**, adresându-se în special **cadrelor didactice**, dar și **angajatorilor** care doresc o imagine clară asupra performanței academice.

Aplicația oferă:

- Vizualizarea datelor studenților
- Adăugarea, editarea și ștergerea studenților (doar de către administrator)
- Calcul automat al mediei și al creditelor
- Exportul bazei de date în format CSV 
- Navigare intuitivă cu căutare, sortare și filtrare după an

---

## Tehnologii utilizate

- **Python + Flask** – pentru logica backend
- **SQLite** – sistem local de baze de date
- **Flask-SQLAlchemy** – ORM pentru manipularea bazei de date
- **Flask-Login** – sistem de autentificare
- **HTML, CSS, JavaScript** – pentru interfață modernă și responsive
- **API IPAPI** – obținerea informațiilor despre locația utilizatorului

---

## Funcționalități principale

- Autentificare administrator
- Vizualizare studenți grupați pe ani (Anul 1, 2, 3)
- Căutare instantanee după nume
- Sortare după medie generală
- Adăugare student cu validare a datelor
- Editare completă a informațiilor și notelor
- Ștergere student
- Calcul automat al mediei și al creditelor
- Export al datelor în format `.csv`
- Mod întunecat (Dark Mode)
- Interfață responsive pentru mobil și tabletă
- Integrare API (ipapi.co) pentru afișarea orașului și țării utilizatorului

---

## Autentificare administrator

Accesul la funcționalitățile de adăugare, editare și ștergere este permis doar administratorului.

**Date implicite pentru testare**:
Username: admin
Parola: parola123

Aceste credențiale pot fi modificate în fișierul `app.py`, în metoda `User.check_credentials()`.

---

## Utilizare pentru cadre didactice

- Vizualizare rapidă a situației academice a studenților
- Căutare și filtrare după an, grupă, medie
- Export în format CSV pentru analiză sau arhivare

---

## Utilizare pentru angajatori

- Acces la informații precum: medie generală, specializare, județ, oraș, email
- Vizualizare note și performanță academică
- Util ca punct de plecare pentru recrutare sau selecție

---

## API public utilizat

Aplicația utilizează API-ul [https://ipapi.co](https://ipapi.co) pentru a identifica:

- IP-ul utilizatorului
- Orașul și țara din care accesează aplicația

---

## Gestionarea erorilor

Aplicația are pagini dedicate pentru:

- **404 – Pagina nu a fost găsită**
- **500 – Eroare internă de server**

Fișierele aferente sunt disponibile în folderul `templates`.

---

## Instrucțiuni pentru rulare locală

1. (Opțional) Creează un mediu virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows


2.Instalarea pachetelor necesare se gaseste in requirments.txt

# pip install -r requirements.txt

3.Rularea aplicatie 

# python app.py

4.Deschiderea in browswer : 
 
 http://127.0.0.1:5000/
 

# Structura Proiectului 
├── app.py               # Logica principală Flask
├── config.py            #Fișier de configurare – definește locația bazei de date și alte opțiuni Flask
├── templates/           # Fișiere HTML (login, index, 404, etc.)
├── static/
│   ├── style.css        # Design modern și responsive
│   └── script.js        # Funcționalități frontend (search, dark mode, API)
├── students.db          # Baza de date SQLite
├── create_db.py         # Script pentru inițializarea bazei de date
├── requirements.txt     # Pachetele necesare pentru rulare
└── README.md            # Acest fișier de documentație

Ion Robert Florin – student anul 3
Facultatea de Informatică, Universitatea Titu Maiorescu
Profesor indrumator Mihai Popescu
