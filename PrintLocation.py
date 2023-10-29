from flask_wtf import FlaskForm as Form
import sqlite3

# class that prints location form
class PrintLocation(Form):
    def __init__(self, form):
        # takes user input and turns it into a dictionary
        d = form.to_dict()

        # set c to user input county
        c = d.get('county')

        # connect to database
        con = sqlite3.connect("user_data.db")
        cursor = con.cursor()

        # select statement
        # find matches from user county input to county
        cursor.execute('SELECT * FROM polls WHERE county = ?', [c])
        con.commit()

        # match = the county match
        match = cursor.fetchone()

        # if match exists
        if match:
            # set variables to matching database positions
            self.name = match[2]
            self.precinct = match[1]
            self.city = match[5]
            self.streetname = match[4]
            self.streetnum = match[3]
            self.county = match[0]
            self.zip = match[6]
            self.state = match[7]
            self.site = match[8]
        
        # if match does not exist
        else:
            # set variables to 0
            self.name = 0
            self.precinct = 0
            self.city = 0
            self.streetname = 0
            self.streetnum = 0
            self.county = 0
            self.zip = 0
            self.state = 0
            self.site = 0

    # pass variables 
    def __call__(self, county, streetname, streetnum, zip, state, name, precinct, city, match, site):
        self.county = county
        self.streetname = streetname
        self.streetnum = streetnum
        self.zip = zip
        self.state = state
        self.name = name
        self.precinct = precinct
        self.city = city
        self.match = match
        self.site = site