from flask import Flask, render_template, request, redirect, url_for, flash, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import csv
import io
from datetime import datetime, date
import re
from flask import jsonify

#  Configurare aplicație Flask + baze de date + autentificare
app = Flask(__name__)
app.secret_key = 'cheie-secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#  Modelul pentru tabela "students"
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nume = db.Column(db.String(100), nullable=False)
    prenume = db.Column(db.String(100), nullable=False)
    data_nasterii = db.Column(db.String(10))
    grupa = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120))
    specializare = db.Column(db.String(100))
    credite = db.Column(db.Integer)
    nota_m1_1 = db.Column(db.Float)
    nota_m1_2 = db.Column(db.Float)
    nota_m2_1 = db.Column(db.Float)
    nota_m2_2 = db.Column(db.Float)
    media = db.Column(db.Float)
    judet = db.Column(db.String(100))
    oras = db.Column(db.String(100))
    an = db.Column(db.String(1))


#  Clasa simplificată pentru utilizator TEST (admin)
class User(UserMixin):
    id = 1

    @staticmethod
    def check_credentials(username, password):
        return username == "admin" and password == "parola123"

# Funcție necesară de Flask-Login pentru încărcarea utilizatorului logat
@login_manager.user_loader
def load_user(user_id):
    if user_id == "1":
        return User()
    return None

@app.context_processor
def inject_user():
    return dict(current_user=current_user)

#  Calculează vârsta pe baza datei de naștere pentru display
def calculeaza_varsta(data_nasterii):
    if data_nasterii:
        try:
            nastere = datetime.strptime(data_nasterii, "%d-%m-%Y").date()
            azi = date.today()
            return azi.year - nastere.year - ((azi.month, azi.day) < (nastere.month, nastere.day))
        except:
            return None
    return None

#  Ruta principală - afișează toți studenții + căutare și sortare
@app.route('/')
def index():
    q = request.args.get('q', '')
    sort_by_media = request.args.get('sort_by_media', '')

    all_students = Student.query.all()
    q = q.lower()

    if q:
        studentii = [
        s for s in all_students
        if q in s.nume.lower()
        or q in s.prenume.lower()
        or q in f"{s.nume} {s.prenume}".lower()
        or q in s.grupa.lower()
        or (s.specializare and q in s.specializare.lower())
        or (s.judet and q in s.judet.lower())
        or (s.oras and q in s.oras.lower())
    ]

    else:
        studentii = all_students


    for student in studentii:
        student.varsta = calculeaza_varsta(student.data_nasterii)

    if sort_by_media == 'asc':
        studentii.sort(key=lambda s: (int(s.an) if s.an else 0, s.media if s.media else -1.0))
    elif sort_by_media == 'desc':
        studentii.sort(key=lambda s: (int(s.an) if s.an else 0, -(s.media if s.media else -1.0)))

    return render_template('index.html', studentii=studentii, selected_sort=sort_by_media)


#  Rută  pentru sugestii autocomplete (suggestionbox) la căutare
@app.route('/autocomplete')
def autocomplete():
    term = request.args.get('term', '').lower()
    if not term:
        return jsonify([])

    students = Student.query.all()
    suggestions = [
        f"{s.nume} {s.prenume}" for s in students
        if term in s.nume.lower() or term in s.prenume.lower()
    ]
    return jsonify(suggestions[:5])

# Exportă întreaga bază de date în format CSV pentru excel / query etc..
@app.route('/export_csv')
@login_required
def export_csv():
    students = Student.query.all()
    si = io.StringIO()
    writer = csv.writer(si)
    writer.writerow(['ID', 'Nume', 'Prenume', 'Data nașterii', 'An', 'Grupa', 'Specializare', 'Credite', 'Media', 'Note', 'Județ', 'Oraș'])
    for s in students:
        writer.writerow([
            s.id, s.nume, s.prenume, s.data_nasterii, s.an, s.grupa, s.specializare,
            s.credite or 0, s.media or 0,
            f"{s.nota_m1_1}, {s.nota_m1_2}, {s.nota_m2_1}, {s.nota_m2_2}",
            s.judet, s.oras
        ])
    output = si.getvalue()
    si.close()
    return Response(output, mimetype='text/csv', headers={'Content-Disposition': 'attachment; filename=studenti.csv'})


#  Pagina de autentificare pentru administrator
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if User.check_credentials(username, password):
            user = User()
            login_user(user)
            flash("Autentificat cu succes!", "success")
            return redirect(url_for('index'))
        else:
            flash("Date incorecte!", "danger")
    return render_template('login.html')


#Pagina Log-out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

#Adaugare student cu validarii
@app.route('/add_student', methods=['POST'])
@login_required
def add_student():
    nume = request.form['nume'].capitalize()
    prenume = request.form['prenume']
    data_nasterii = request.form['data_nasterii']
    grupa = request.form['grupa']
    an = request.form['an']
    email = request.form.get('email', '')
    specializare = request.form.get('specializare', '')
    judet = request.form.get('judet', '')
    oras = request.form.get('oras', '')

    if not re.fullmatch(r'[A-Z][a-z]+', nume):
        flash('Numele trebuie să înceapă cu literă mare și să conțină doar litere.', 'danger')
        return redirect(url_for('index'))
    if not re.fullmatch(r'[A-Za-z ]+', prenume):
        flash('Prenumele trebuie să conțină doar litere și spații.', 'danger')
        return redirect(url_for('index'))
    if specializare not in ['Informatica', 'Drept']:
        flash('Specializarea este invalidă.', 'danger')
        return redirect(url_for('index'))

    # ✅ forma data valida 
    try:
        datetime.strptime(data_nasterii, '%d-%m-%Y')
    except ValueError:
        flash('Formatul datei de naștere trebuie să fie DD-MM-YYYY.', 'danger')
        return redirect(url_for('index'))


    student = Student(
        nume=nume,
        prenume=prenume,
        data_nasterii=data_nasterii,
        grupa=grupa,
        an=an,
        email=email,
        specializare=specializare,
        judet=judet,
        oras=oras,
        credite=0,
        nota_m1_1=None,
        nota_m1_2=None,
        nota_m2_1=None,
        nota_m2_2=None,
        media=None
    )
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('index', success=1))

#validare edit_student
@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_student(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.nume = request.form['nume']
        student.prenume = request.form['prenume']
        student.data_nasterii = request.form['data_nasterii']
        student.an = request.form['an']
        student.grupa = request.form['grupa']
        student.email = request.form.get('email', '')
        student.specializare = request.form.get('specializare', '')
        student.judet = request.form.get('judet', '')
        student.oras = request.form.get('oras', '')

        #  (verificare float și calcul)
        try:
            student.nota_m1_1 = float(request.form.get('nota_m1_1') or 0)
            student.nota_m1_2 = float(request.form.get('nota_m1_2') or 0)
            student.nota_m2_1 = float(request.form.get('nota_m2_1') or 0)
            student.nota_m2_2 = float(request.form.get('nota_m2_2') or 0)
        except ValueError:
            flash('Notele trebuie să fie valori numerice.', 'danger')
            return redirect(url_for('edit_student', id=student.id))

        # Calculează media și creditele (logica simpla de 15max)
        note = [student.nota_m1_1, student.nota_m1_2, student.nota_m2_1, student.nota_m2_2]
        note_valide = [n for n in note if n > 0]
        student.media = round(sum(note_valide) / len(note_valide), 2) if note_valide else None
        student.credite = min(sum(5 for n in note if n >= 5), 15)

        db.session.commit()
        flash('Student actualizat cu succes!', 'success')
        return redirect(url_for('index'))

    return render_template('edit_student.html', student=student)


@app.route('/delete_student/<int:id>', methods=['GET'])
@login_required
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index', deleted=1))


#Calculator varsta cu datetime simplu 
def calculeaza_varsta(data_nasterii):
    try:
        data = datetime.strptime(data_nasterii, '%d-%m-%Y')
        azi = datetime.today()
        return azi.year - data.year - ((azi.month, azi.day) < (data.month, data.day))
    except:
        return None

@app.route('/student_details/<int:id>', methods=['GET'])
def student_details(id):
    student = Student.query.get_or_404(id)
    varsta = calculeaza_varsta(student.data_nasterii)
    return render_template('student_details.html', student=student, varsta=varsta)


@app.route('/adauga_note/<int:id>', methods=['GET'])
@login_required
def show_adauga_note(id):
    student = Student.query.get_or_404(id)
    return render_template('adauga_note.html', student=student)


#Adaugare note 
@app.route('/adauga_note/<int:id>', methods=['POST'])
@login_required
def adauga_note(id):
    student = Student.query.get_or_404(id)

    try:
        student.nota_m1_1 = float(request.form.get('nota_m1_1') or 0)
        student.nota_m1_2 = float(request.form.get('nota_m1_2') or 0)
        student.nota_m2_1 = float(request.form.get('nota_m2_1') or 0)
        student.nota_m2_2 = float(request.form.get('nota_m2_2') or 0)

        note = [student.nota_m1_1, student.nota_m1_2, student.nota_m2_1, student.nota_m2_2]
        media_valide = [n for n in note if n > 0]
        student.media = round(sum(media_valide) / len(media_valide), 2) if media_valide else None

        student.credite = min(15, sum(5 for n in note if n >= 5))  # Max 15 credite

        db.session.commit()
        flash("Note salvate cu succes!", "success")
    except Exception as e:
        flash(f"Eroare la salvare: {str(e)}", "danger")

    return redirect(url_for('index'))


#GESTIONARE DE ERORII HTTP : 404  . 500 
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


#Initializarea bazei de date si pornirea aplicatiei
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)






