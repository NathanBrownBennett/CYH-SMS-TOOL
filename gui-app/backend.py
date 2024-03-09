from flask import Flask, request, render_template, redirect, url_for, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

users = {
    'mr.user@email.com': '7310289491'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data['message']
    
    if 'state' not in session:
        session['state'] = 'START'
    
    # Process the message as per your application's logic
    reply = process_message(message)
    
    return jsonify(reply=reply)

def process_message(message):
    state = session['state']
    username = session.get('username')
    
    if state == 'START':
        reply = "Welcome to the CYH SMS Tool Interface. \n1. Login\n2. Create an account"
        session['state'] = 'LOGIN'
    
    elif state == 'LOGIN':
        if message.strip() == '1':
            reply = "Enter your username:"
            session['state'] = 'AWAITING_USERNAME'
        elif message.strip() == '2':
            reply = "Enter a new username:"
            session['state'] = 'AWAITING_NEW_USERNAME'
        else:
            reply = "Invalid choice. Please try again."

    elif state == 'AWAITING_USERNAME':
        session['temp_username'] = message.strip()
        reply = "Enter your password:"
        session['state'] = 'AWAITING_PASSWORD'

    elif state == 'AWAITING_PASSWORD':
        if users.get(session['temp_username']) == message:
            session['username'] = session['temp_username']
            reply = "Login successful!\n1. View your groups\n2. Receive the latest updates from the platform today\n3. Open your conversations\n4. Settings"
            session['state'] = 'LOGGED_IN'
        else:
            reply = "Login failed. Invalid username or password."
            session['state'] = 'START'

    # More states like 'AWAITING_NEW_USERNAME', 'LOGGED_IN', etc., would be handled here

    else:
        reply = "An error has occurred."
        session['state'] = 'START'

    return reply

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
    app.run(debug=True , host='0.0.0.0', port=5001)
