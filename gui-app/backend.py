from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

users = {
    'mr.user@email.com': '7310289491'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['user'] = username
            return redirect(url_for('main_menu'))
        else:
            return 'Login failed', 401
    return render_template('login.html')

@app.route('/menu', methods=['GET'])
def main_menu():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('menu.html')

@app.route('/poll', methods=['GET', 'POST'])
def handle_poll():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        poll_choice = request.form['poll_choice']
        # Here, you would record the poll choice in the database or session
        session['poll_response'] = poll_choice
        return redirect(url_for('main_menu'))
    return render_template('poll.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0')
