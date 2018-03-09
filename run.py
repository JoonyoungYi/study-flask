from flask import Flask, jsonify, render_template, flash, url_for, redirect, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
import config
app.config.from_object(config)
app.secret_key = app.config.get('SECRET_KEY')
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(50))
    text = db.Column(db.String(1024))

@app.route("/")
def show_entries():
    entries = Entry.query.order_by(Entry.id.desc()).all()
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    entry = Entry()
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.add(entry)

    db.session.commit()

    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == "__main__":
    #db.drop_all()
    #db.create_all()
    app.run(debug=True)
