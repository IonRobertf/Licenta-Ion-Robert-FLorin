#Populate folosit ca exemplu pentru incarcarea de date.
from app import db, Student, app
with app.app_context():
    
    sample_students = [
    {
            "nume": "Radu", "prenume": "Elena", "data_nasterii": "16-10-2002", "an": "2",
            "grupa": "202B", "email": "elena.radu22@example.com", "specializare": "Informatica",
            "judet": "Iași", "oras": "Cluj-Napoca", "note": [4.9, 6.8, 5.5, 5.5]
        },
        {
            "nume": "Popescu", "prenume": "Vlad", "data_nasterii": "12-10-2002", "an": "2",
            "grupa": "201A", "email": "vlad.popescu37@example.com", "specializare": "Drept",
            "judet": "Galați", "oras": "Iași", "note": [5.8, 9.8, 8.1, 6.7]
        },
        {
            "nume": "Enache", "prenume": "Robert", "data_nasterii": "19-06-2002", "an": "2",
            "grupa": "201A", "email": "robert.enache50@example.com", "specializare": "Drept",
            "judet": "Dolj", "oras": "Cluj-Napoca", "note": [7.4, 10.0, 5.8, 9.9]
        },
        {
            "nume": "Neagu", "prenume": "Alex", "data_nasterii": "25-04-2002", "an": "2",
            "grupa": "202B", "email": "alex.neagu2@example.com", "specializare": "Drept",
            "judet": "Argeș", "oras": "București", "note": [7.6, 6.1, 7.8, 7.7]
        },
        {
            "nume": "Stan", "prenume": "Maria", "data_nasterii": "19-06-2002", "an": "2",
            "grupa": "202B", "email": "maria.stan81@example.com", "specializare": "Informatica",
            "judet": "București", "oras": "Brașov", "note": [8.4, 4.5, 5.8, 8.5]
        },
        {
            "nume": "Stan", "prenume": "Robert", "data_nasterii": "09-08-2002", "an": "2",
            "grupa": "202B", "email": "robert.stan17@example.com", "specializare": "Informatica",
            "judet": "Galați", "oras": "Constanța", "note": [9.8, 5.8, 9.2, 8.8]
        },
        {
            "nume": "Florea", "prenume": "Maria", "data_nasterii": "26-07-2002", "an": "2",
            "grupa": "202B", "email": "maria.florea19@example.com", "specializare": "Informatica",
            "judet": "Timiș", "oras": "Ploiești", "note": [4.1, 7.2, 6.7, 8.0]
        },
        {
            "nume": "Enache", "prenume": "Bianca", "data_nasterii": "01-10-2002", "an": "2",
            "grupa": "201A", "email": "bianca.enache49@example.com", "specializare": "Drept",
            "judet": "Constanța", "oras": "Cluj-Napoca", "note": [9.3, 7.4, 9.5, 5.3]
        },
        {
            "nume": "Ionescu", "prenume": "Vlad", "data_nasterii": "02-01-2002", "an": "2",
            "grupa": "201A", "email": "vlad.ionescu90@example.com", "specializare": "Informatica",
            "judet": "Brașov", "oras": "Ploiești", "note": [5.8, 7.0, 4.6, 9.3]
        },
        {
            "nume": "Stan", "prenume": "Ioana", "data_nasterii": "14-11-2002", "an": "2",
            "grupa": "202B", "email": "ioana.stan59@example.com", "specializare": "Informatica",
            "judet": "Constanța", "oras": "Galați", "note": [4.6, 6.9, 6.4, 9.7]
        },
        {
            "nume": "Popescu", "prenume": "Cristina", "data_nasterii": "04-11-2001", "an": "3",
            "grupa": "301A", "email": "cristina.popescu28@example.com", "specializare": "Drept",
            "judet": "Dolj", "oras": "Craiova", "note": [6.2, 9.4, 7.9, 4.4]
        },
        {
            "nume": "Enache", "prenume": "Robert", "data_nasterii": "02-06-2001", "an": "3",
            "grupa": "301A", "email": "robert.enache16@example.com", "specializare": "Informatica",
            "judet": "Dolj", "oras": "Cluj-Napoca", "note": [5.5, 4.8, 7.4, 4.4]
        },
        {
            "nume": "Georgescu", "prenume": "Robert", "data_nasterii": "26-10-2001", "an": "3",
            "grupa": "302B", "email": "robert.georgescu76@example.com", "specializare": "Informatica",
            "judet": "Timiș", "oras": "Timișoara", "note": [4.0, 9.2, 4.9, 4.8]
        },
        {
            "nume": "Enache", "prenume": "Elena", "data_nasterii": "26-04-2001", "an": "3",
            "grupa": "301A", "email": "elena.enache15@example.com", "specializare": "Drept",
            "judet": "București", "oras": "Iași", "note": [7.5, 4.1, 5.6, 4.8]
        },
        {
            "nume": "Neagu", "prenume": "Stefan", "data_nasterii": "17-10-2001", "an": "3",
            "grupa": "302B", "email": "stefan.neagu15@example.com", "specializare": "Drept",
            "judet": "Cluj", "oras": "Craiova", "note": [4.7, 7.0, 9.7, 4.3]
        },
        {
            "nume": "Georgescu", "prenume": "Alex", "data_nasterii": "14-11-2001", "an": "3",
            "grupa": "302B", "email": "alex.georgescu59@example.com", "specializare": "Drept",
            "judet": "București", "oras": "București", "note": [4.6, 8.3, 6.7, 9.4]
        },
        {
            "nume": "Matei", "prenume": "Bianca", "data_nasterii": "13-10-2001", "an": "3",
            "grupa": "302B", "email": "bianca.matei19@example.com", "specializare": "Drept",
            "judet": "Cluj", "oras": "Iași", "note": [7.2, 6.7, 7.6, 4.6]
        },
        {
            "nume": "Ionescu", "prenume": "Stefan", "data_nasterii": "14-06-2001", "an": "3",
            "grupa": "302B", "email": "stefan.ionescu93@example.com", "specializare": "Informatica",
            "judet": "Timiș", "oras": "Ploiești", "note": [9.0, 6.4, 8.4, 5.9]
        },
        {
            "nume": "Matei", "prenume": "Alex", "data_nasterii": "27-02-2001", "an": "3",
            "grupa": "301A", "email": "alex.matei48@example.com", "specializare": "Informatica",
            "judet": "Iași", "oras": "Craiova", "note": [4.6, 4.6, 8.4, 8.9]
        },
        {
            "nume": "Georgescu", "prenume": "Andrei", "data_nasterii": "14-06-2001", "an": "3",
            "grupa": "302B", "email": "andrei.georgescu76@example.com", "specializare": "Informatica",
            "judet": "Galați", "oras": "Galați", "note": [9.2, 9.6, 6.5, 9.5]
        }

]

    

    for s in sample_students:
        note = s["note"]
        media = round(sum(note) / len(note), 2)
        credite = sum(5 for n in note if n >= 5)

        student = Student(
            nume=s["nume"],
            prenume=s["prenume"],
            data_nasterii=s["data_nasterii"],
            grupa=s["grupa"],
            an=s["an"],
            email=s["email"],
            specializare=s["specializare"],
            judet=s["judet"],
            oras=s["oras"],
            nota_m1_1=note[0],
            nota_m1_2=note[1],
            nota_m2_1=note[2],
            nota_m2_2=note[3],
            media=media,
            credite=min(credite, 15)
        )
        db.session.add(student)

    db.session.commit()
    print("✔️ Studenți de test adăugați cu succes!")
