from flask import Flask, render_template_string, request, redirect, url_for, session, flash, render_template, Response, send_file, abort
import pdfkit 
import db
import datetime
import pickle
import base64
from urllib.request import urlopen

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bruh'

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route('/', methods=['GET'])
def bruh():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = db.get_user(username, password)
        if result:
            user = User(result[0], result[1])
            session['user'] = base64.b64encode(pickle.dumps(user)).decode()
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'info')
        return render_template('login.html')
    if 'user' in session:
        username = session['user']
        return redirect(url_for('home'))
    return render_template('login.html')
        

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' in session:
        try:
            d64 = base64.b64decode(session['user'].encode())
            user = pickle.loads(d64)
            username = user.username
            if request.method == 'POST':
                localtime = datetime.datetime.now()
                time = '' + str("%02d"%localtime.day) + '-' + str("%02d"%localtime.month) + '-' + str(localtime.year) + ' At ' + str("%02d"%localtime.hour) + ':' + str("%02d"%localtime.minute)
                comment = request.form['comment']
                db.add_comment(username, comment, time)

            results = db.get_comments() 
            return render_template('home.html', comments=results)
        except:
            return "Don't hack!!!"
    else:
        return redirect(url_for('login'))

@app.route('/search_url', methods=['GET', 'POST'])
def search_url():
    if 'user' in session:
        if request.method == 'POST':
            url = request.form['url']
            search_result = ''
            if not url:
                flash('Please provide a URL', 'info')
            else:
                try:
                    out = urlopen(url).read()
                    search_result = out
                except:
                    flash('Unable to fetch URL', 'info')
            urlout = render_template_string(url)
            return render_template('search_url.html', url=urlout,search_result=search_result)
        return render_template('search_url.html')
    else: 
        return redirect(url_for('login'))
    
@app.route('/search_user', methods=['GET'])
def search_user():
    if 'user' in session:
        if request.method == 'GET' and request.args.get('name'):
            search_name = request.args.get('name')
            if not search_name:
                flash('Please provide a username', 'info')
            elif '<' in search_name or '>' in search_name or '\'' in search_name:
                abort(403, description="Hackedddddddd!!!!!!!!!!!!!!!!")
            else:
                results = db.get_users(search_name)
                if results == []:
                    flash('User not found', 'info')
                return render_template('search_user.html', users=results)
        return render_template('search_user.html')
    else: 
        return redirect(url_for('login'))

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'user' in session:
        if request.method == 'POST':
            new_password = request.form['newPassword']
            repeat_password = request.form['repeatPassword']
            if not new_password or not repeat_password:
                flash('Please provide new password and repeat password', 'info')
            elif new_password != repeat_password:
                flash('Repeat password is not the same as new password', 'info')
            else:
                d64 = base64.b64decode(session['user'].encode())
                user = pickle.loads(d64)
                username = user.username
                db.edit_userPassword(username, new_password)
                session.pop('user', None)
                return '<script>alert("Updated password successfully")</script>'
        return render_template('change_password.html')
    else: 
        return redirect(url_for('login'))

@app.route('/message_pdf', methods=['GET', 'POST'])
def message_pdf():
    if 'user' in session:
        if request.method == 'POST':
            message = request.form['message']
            if not message:
                flash('Please provide a message', 'info')
            else:
                pdfkit.from_string(message, 'nam.pdf')
                return send_file('../nam.pdf', as_attachment=True)
        return render_template('message_pdf.html')
    else: 
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=6379)

