from flask import Flask, render_template_string, request, redirect, url_for, session, flash, render_template
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
                time = str("%02d"%localtime.day) + '-' + str("%02d"%localtime.month) + '-' + str(localtime.year) + ' At ' 
                + str("%02d"%localtime.hour) + ':' + str("%02d"%localtime.minute)
                db.add_comment(username, request.form['comment'], time)

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
            urlout = render_template_string('The result ' + url + ' is:')
            return render_template('search_url.html', url=urlout,search_result=search_result)
        return render_template('search_url.html')
    else: 
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=6379)

