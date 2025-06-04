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