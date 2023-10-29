### Sophie Hasara, Aakriti Shah, James McIntyre, Alex Hernandez ###
### driver class for all operations of application ###

from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from PopQuiz import PopQuiz
import sqlite3
import logging
from PrintScore import PrintScore
from PollLocation import PollLocation
from LocationForm import LocationForm
from LoginForm import LoginForm
from PrintLocation import PrintLocation
from RegisterForm import RegisterForm
from Quiz import Quiz


# for debugging purposes
logging.basicConfig(filename='record.log', level=logging.DEBUG)

# Flask <- app
app = Flask(__name__)

# connect to database with pathfile
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/aakritishah/Desktop/user_data.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

# db <- app
db = SQLAlchemy(app)

# connect flask session 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

## route to welcome page
@app.route('/')
def index():
    # render welcome template
    return render_template('index.html')

## route sign up page
@app.route('/signup', methods=['GET', 'POST'])
def signuppage():
    # print the form on to page when it is rendered
    form = RegisterForm()
    # if the user has input their username and password
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # for debugging purposes
        app.logger.info("signuppage function called")

        # set variables
        username = request.form['username']
        password = request.form['password']

        # make database connection
        con = sqlite3.connect("user_data.db")
        cursor = con.cursor()

        # select statement 
        # check database for where username matches
        cursor.execute('SELECT * FROM users WHERE username = ?', [username])
        con.commit()

        # user = all instances where username matches
        user = cursor.fetchone()

        # if instances exist
        if user:
            # generate sign up error 
            return render_template('signuperror.html', form=form)
        
        # if the username or password is not entered
        elif not username or not password:
            # generate sign up error
            return render_template('signuperror.html', form=form)

        # if no instances exist and username/password is not entered
        else:
            # login success: insert new user into database
            cursor.execute('INSERT INTO users (username, password) VALUES (:username, :password)', [username, password])
            con.commit()

            # render signed up template with new form to login
            form = LoginForm()
            return render_template('signedup.html', form=form)
    # render sign up template with registration form
    return render_template('signup.html', form=form)

## route login page
@app.route('/login', methods=['GET', 'POST'])
def loginpage():
    # print the form on to page when it is rendered
    form = LoginForm()
    # if the user has input their username and password
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # set variables
        username = request.form['username']
        password = request.form['password']
        
        # for debugging purposes
        app.logger.info("loginpage function called")

        # make database connection
        con = sqlite3.connect("user_data.db")
        cursor = con.cursor()

        # select statement 
        # check database for where username and password matches
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [username, password])
        con.commit()

        # user = all instances where username and password match
        user = cursor.fetchone()

        # if matching instances exist
        if user:
            # session set to True
            session['logged_in'] = True
            
            # set session name to username
            session["name"] = user[1]

            # set session id to user id
            session["id"] = user[0]
            # render account template and pass user's username as name
            return render_template('account.html', name=username)
        
        # if matching instances dont exist
        else:
            # render login fail page
            return render_template('nologin.html')
    
    # render login template with login form
    return render_template('login.html', form=form)

## route take quiz page
@app.route('/takequiz', methods=['GET','POST'])
def takequizpage():
    # print the form on to page when it is rendered
    form = PopQuiz()

    # render login template with quiz form
    return render_template('quiz.html', form=form)

## route val demings alignment page
@app.route('/val')
def val():
    # set name to Val
    name = "Val Demings"

    # connect to database 
    con = sqlite3.connect("user_data.db")
    cursor = con.cursor()

    # select statement 
    # check database for where name matches
    cursor.execute('SELECT * FROM candidates WHERE name = ?', [name])
    con.commit()

    # cand = instance where name matches
    cand = cursor.fetchone()

    # set variables to matching database values
    state = cand[3]
    party = cand[1]
    run = cand[4]
    bio = cand[2]
    site = cand[6]

    # for debugging purposes
    app.logger.debug(bio)
    # render candidate template with varibles for Val passed
    return render_template('cand.html', name=name, bio=bio, state=state, party=party, run=run, site=site)

## route marco rubio alignment page
@app.route('/marco')
def marco():
    # set name to Marco
    name = "Marco Rubio"

    # connect to database 
    con = sqlite3.connect("user_data.db")
    cursor = con.cursor()

    # select statement 
    # check database for where name matches
    cursor.execute('SELECT * FROM candidates WHERE name = ?', [name])
    con.commit()

    # cand = instance where name matches
    cand = cursor.fetchone()

    # set variables to matching database values
    state = cand[3]
    party = cand[1]
    run = cand[4]
    bio = cand[2]
    site = cand[6]

    # for debugging purposes
    app.logger.debug(bio)
    # render candidate template with varibles for Marco passed
    return render_template('cand.html', name=name, bio=bio, state=state, party=party, run=run, site=site)

## route charlie crist alignment page
@app.route('/charlie')
def charlie():
    # set name to Charlie
    name = "Charlie Crist"

    # connect to database 
    con = sqlite3.connect("user_data.db")
    cursor = con.cursor()

    # select statement 
    # check database for where name matches
    cursor.execute('SELECT * FROM candidates WHERE name = ?', [name])
    con.commit()

    # cand = instance where name matches
    cand = cursor.fetchone()

    # set variables to matching database values
    state = cand[3]
    party = cand[1]
    run = cand[4]
    bio = cand[2]
    site = cand[6]

    # for debugging purposes
    app.logger.debug(bio)
    # render candidate template with varibles for Charlie passed
    return render_template('cand.html', name=name, bio=bio, state=state, party=party, run=run, site=site)

## route ron desantis alignment page
@app.route('/ron')
def ron():
    # set name to Ron
    name = "Ron Desantis"

    # connect to database 
    con = sqlite3.connect("user_data.db")
    cursor = con.cursor()

    # select statement 
    # check database for where name matches
    cursor.execute('SELECT * FROM candidates WHERE name = ?', [name])
    con.commit()

    # cand = instance where name matches
    cand = cursor.fetchone()

    # set variables to matching database values
    state = cand[3]
    party = cand[1]
    run = cand[4]
    bio = cand[2]
    site = cand[6]

    # for debugging purposes
    app.logger.debug(bio)
    # render candidate template with varibles for Ron passed
    return render_template('cand.html', name=name, bio=bio, state=state, party=party, run=run, site=site)   

## route representative candidate #1 alignment page
@app.route('/cand1')
def candidate1():
    # print the form on to page when it is rendered
    form = PrintScore(request.form)

    # set district to the user's response
    district = form.dist1

    # connect to database
    con = sqlite3.connect("user_data.db")
    cursor = con.cursor()

    # select statement
    # check database for where district matches
    cursor.execute('SELECT * FROM candidates WHERE district = ?', [district])
    con.commit()

    # cand = instances that exist where district matches
    cand = cursor.fetchall()

    # set variables to matching database values
    name = cand[0][0]
    state = cand[0][3]
    party = cand[0][1]
    run = cand[0][4]
    bio = cand[0][2]
    dist = cand[0][5]
    site = cand[0][6]
    # render candidate template with varibles for candidate #1 are passed
    return render_template('repcand.html', name=name, bio=bio, state=state, party=party, run=run, dist=dist, site=site)

## route representative candidate #2 alignment page
@app.route('/cand2')
def candidate2():
    # print the form on to page when it is rendered
    form = PrintScore(request.form)

    # set district to the user's response
    district = form.dist1

    # connect to database
    con = sqlite3.connect("user_data.db")
    cursor = con.cursor()

    # select statement
    # check database for where district matches
    cursor.execute('SELECT * FROM candidates WHERE district = ?', [district])
    con.commit()

    # cand = instances that exist where district matches
    cand = cursor.fetchall()

    # set variables to matching database values
    name = cand[0][0]
    state = cand[0][3]
    party = cand[0][1]
    run = cand[0][4]
    bio = cand[0][2]
    dist = cand[0][5]
    site = cand[0][6]
    # render candidate template with varibles for candidate #2 are passed
    return render_template('repcand.html', name=name, bio=bio, state=state, party=party, run=run, dist=dist, site=site)

## render results page
@app.route('/results',methods=['GET','POST'])
def resultspage():
    # print the form on to page when it is rendered
    form = PrintScore(request.form)

    # gather all inputs and set them to variables
    site1 = form.site1
    site2 = form.site2
    rotatec1 = form.rotatecand1
    rotatec2 = form.rotatecand2
    c1name = form.cand1
    c2name = form.cand2
    cand1score = form.cand1score
    cand2score = form.cand2score
    rscore = form.rightscore
    lscore = form.leftscore
    iscore = form.indscore
    dist = form.dist1

    # rotate value for the css animation
    rotatev = form.rotateval
    rotatem = form.rotatemarc
    rotatec = form.rotatechar
    rotater = form.rotateron

    # senators
    sen1 = form.valalign
    sen2 = form.marcalign

    # governers
    gov1 = form.charalign
    gov2 = form.ronalign

    # get session
    if session.get('logged_in'):
        # if user is logged in
        if session["logged_in"] == True:
            # connect to database
            con = sqlite3.connect("user_data.db")
            cursor = con.cursor()
            
            # insert statement
            # insert quiz results into table
            cursor.execute('INSERT INTO quizHistory (user_id, rightscore, leftscore, indscore) VALUES (:user_id, :rscore, :lscore, :iscore)', [session["id"], rscore, lscore, iscore])
            con.commit()
    
    # render result alignment template with variables are passed
    return render_template('aligns.html', rscore=rscore, lscore=lscore, iscore=iscore, sen1=sen1, sen2=sen2, gov2=gov2, gov1=gov1, rotatev=rotatev, rotatem=rotatem, rotater=rotater, rotatec=rotatec, rotatec1=rotatec1, rotatec2=rotatec2, c1name=c1name, c2name=c2name, cand1score=cand1score, cand2score=cand2score, dist=dist, site1=site1, site2=site2)
    
## render history page
@app.route('/history', methods=['GET', 'POST'])
def historypage():
    # if session exists
    if session:
        # connect to database
        con = sqlite3.connect("user_data.db")
        cursor = con.cursor()

        # select statement
        # check database for where user id matches session id
        cursor.execute('SELECT * FROM quizHistory WHERE user_id = ?', [session["id"]])

        # history = instances that exist where user id matches session id
        history = cursor.fetchall()

        # if instances exist
        if history:
            # set name to session name
            name = session["name"]
            # render quiz history page and pass in name and history
            return render_template('quizHistory.html', history=history, name=name)
        # if instances dont exist
        else:
            # set name to session name
            name = session["name"]
            # render quiz history page and pass in name
            return render_template('quizHistory.html', name=name)
    else:
        # render login error template
        return render_template('nologin.html')

## render pdf page
@app.route('/pdf',methods=['GET','POST'])
def pdfpage():
    # get session status
    if session.get('logged_in'):
        # if status exists
        if session["logged_in"] == True:
            # render pdf 
            return render_template('pdf.html')
    # otherwise render must sign in template
    return render_template('mustsign.html')

## render find poll location page
@app.route('/findpoll', methods=['GET', 'POST'])
def findpollpage():
    # print form when page is rendered
    form = LocationForm()
    # render page with form passed in
    return render_template('findpoll.html', form=form)

## render location page
@app.route('/location', methods=['GET', 'POST'])
def location():
    # print the location form on to page when it is rendered
    form = PrintLocation(request.form)
    
    # if county exists
    if form.county != 0:
        county = form.county
        zip = form.zip
        streetnum = form.streetnum
        streetname = form.streetname
        state = form.state
        precinct = form.precinct
        city = form.city
        name = form.name
        site = form.site

    # if county does not exist
    else:
        # print location form when page is rendered
        form = LocationForm()
        # render template for find location
        return render_template('findpoller.html', form=form)
    # render location template and pass variables
    return render_template('location.html', county=county, zip=zip, state=state, streetnum=streetnum, streetname=streetname, name=name, precinct=precinct, city=city, site=site)

## render exit page
@app.route('/exit')
def exit():
    # get session status
    if session.get('logged_in'):
        # if user is logged in set to logged out
        session["logged_in"] == False
        # clear the session
        session.clear()
    # render welcome page
    return render_template('index.html')

## main: run app
if __name__ == '__main__':
    app.run(debug=True)