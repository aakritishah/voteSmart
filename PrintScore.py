from flask_wtf import FlaskForm as Form
import sqlite3
import logging
logging.basicConfig(filename='record.log', level=logging.DEBUG)

# class that prints score from form
class PrintScore(Form):
    leftscore = 0
    rightscore = 0
    indscore = 0
    valalign = 0
    marcalign = 0
    ronalign = 0
    charalign = 0
    candidates = []

    def __init__(self, form):
        # takes user input and turns it into a dictionary
        d = form.to_dict()

        # 3 accounts for first two questions and submit button
        questionnum = (len(d) - 3)

        # for representatives by district
        # get user input for district
        district = d.get('district')

        # connect to database
        con = sqlite3.connect("user_data.db")
        cursor = con.cursor()

        # select statement
        # select instances from databases where district == user input district
        cursor.execute('SELECT * FROM candidates WHERE district = ?', [district])

        # cands = matching district values
        cands = cursor.fetchall()

        # if instances exist
        if cands:
            # set variables equal to database values
            self.cand1 = cands[0][0]
            logging.debug(self.cand1)
            self.cand2 = cands[1][0]
            self.party1 = cands[0][1]
            self.party2 = cands[1][1]
            self.bio1 = cands[0][2]
            self.bio2 = cands[1][2]
            self.state1 = cands[0][3]
            self.state2 = cands[1][3]
            self.run1 = cands[0][4]
            self.run2 = cands[1][4]
            dist1 = cands[0][5]
            self.dist1 = dist1
            dist2 = cands[1][5]
            self.dist2 = dist2
            self.site1 = cands[0][6]
            self.site2 = cands[1][6]

        # if instances dont exist
        else:
            # set varaibles to 0 or 'N/A'
            self.cand1 = 'N/A'
            self.cand2 = 'N/A'
            self.dist1 = 0
            self.dist2 = 0

        # dictionaries of candidate alignment 'answer keys'
        dict = {'1': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '2': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"}, 
        '3': {"q1":"No","q2":"Yes","q3":"No","q4":"No","q5":"No","q6":"Yes","q7":"No","q8":"No","q9":"No","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"}, 
        '4': {"q1":"No","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"}, 
        '5': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"}, 
        '6': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"Yes","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '7': {"q1":"Yes","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '8': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '9': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '10': {},
        '11': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '12': {"q1":"No","q2":"Yes","q3":"No","q4":"No","q5":"Yes","q6":"No","q7":"No","q8":"Yes","q9":"Yes","q10":"No","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '13': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '14': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '15': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '16': {"q1":"No","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '17': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '18': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '19': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '20': {"q1":"No","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"No","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '21': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '22': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"No","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '23': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '24': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"No","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '25' : {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '26': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '27': {"q1":"Yes","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '28': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"No","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '29': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '30': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '31': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"Yes","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '32': {"q1":"No","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '33': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '34': {"q1":"No","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '35': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '36': {"q1":"Yes","q2":"No","q3":"No","q4":"Yes","q5":"Yes","q6":"Yes","q7":"Yes","q8":"No","q9":"Yes","q10":"No","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"No","q18":"Pro-Life"},
        '37': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '38': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"No","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '39': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '40': {"q1":"No","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '41': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '42': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '43': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"Yes","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '44': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"YNo","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '45': {"q1":"Yes","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '46': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '47': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '48': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '49': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"No","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '50': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '51': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '52': {"q1":"No","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '53': {"q1":"No","q2":"No","q3":"No","q4":"No","q5":"Yes","q6":"Yes","q7":"Yes","q8":"No","q9":"Yes","q10":"Yes","q11":"Yes","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '54': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"Yes","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"},
        '55': {"q1":"No","q2":"No","q3":"No","q4":"Yes","q5":"Yes","q6":"Yes","q7":"No","q8":"No","q9":"Yes","q10":"Yes","q11":"No","q12":"No","q13":"No","q14":"Yes","q15":"Yes","q16":"Yes","q17":"Yes","q18":"Pro-Life"},
        '56': {"q1":"Yes","q2":"Yes","q3":"Yes","q4":"Yes","q5":"No","q6":"Yes","q7":"Yes","q8":"Yes","q9":"Yes","q10":"Yes","q11":"No","q12":"Yes","q13":"No","q14":"Yes","q15":"Yes","q16":"No","q17":"Yes","q18":"Pro-Choice"}}

        # if questions were answered by user
        if questionnum != 0:

            # candidate 1 alignment calculation
            var = dist1 - 1
            d1 = (dist1 - var) + 4
            if dist1 == 1:
                d1 = dist1
            d1 = str(d1)
            dict1 = dict[d1]
            cand1_shared = {k: dict1[k] for k in dict1 if k in d and dict1[k] == d[k]}
            lencand1 = len(cand1_shared)
            self.cand1score = "{0:.0%}".format(lencand1/questionnum)
            self.rotatecand1 = (lencand1/questionnum) * 180
            
            # candidate 2 alignment calculation
            d2 = dist2 * 2
            d2 = str(d2)
            dict2 = dict[d2]
            cand2_shared = {k: dict2[k] for k in dict2 if k in d and dict2[k] == d[k]}
            lencand2 = len(cand2_shared)
            self.cand2score = "{0:.0%}".format(lencand2/questionnum)
            self.rotatecand2 = (lencand2/questionnum) * 180
            logging.debug('DICT2')
            logging.debug(d2)
            logging.debug(dict2)
            logging.debug(self.cand2score)
            logging.debug(self.rotatecand2)
            logging.debug(dict1)
        
        # if no questions were answered by user
        else:
            # set variables equal to 0
            self.cand1 = "{0:.0%}".format(0)
            self.cand2 = "{0:.0%}".format(0)
            self.party1 = "{0:.0%}".format(0)
            self.party2 = "{0:.0%}".format(0)
            self.bio1 = "{0:.0%}".format(0)
            self.bio2 = "{0:.0%}".format(0)
            self.state1 = "{0:.0%}".format(0)
            self.state2 = "{0:.0%}".format(0)
            self.run1 = "{0:.0%}".format(0)
            self.run2 = "{0:.0%}".format(0)
            self.dist1 = 0
            self.dist2 = "{0:.0%}".format(0)
            self.site1 = "{0:.0%}".format(0)
            self.site2 = "{0:.0%}".format(0)
            dict1 = "{0:.0%}".format(0)
            dict2 = "{0:.0%}".format(0)
            self.rotatecand1 = "{0:.0%}".format(0)
            self.rotatecand2 = "{0:.0%}".format(0)
            self.cand1score = 0
            self.cand2score = 0


        # if questions were answered by user
        if questionnum != 0:

            # right wing alignment calculation
            rightwing = {"q1":"Yes", "q2":"No", "q3":"Yes", "q4":"No", "q5":"Yes", "q6":"No", "q7":"No", "q8":"No", "q9":"No", "q10":"Yes", "q11":"Yes", "q12":"No", "q13":"Yes", "q14":"Yes", "q15":"No", "q16":"Yes", "q17":"No", "q18":"Pro-Life"}
            # calculate alignment by comparing user input dict to answer key dict
            right_shared = {k: rightwing[k] for k in rightwing if k in d and rightwing[k] == d[k]}
            # number of shared values in dictionary comparison
            right = len(right_shared)
            self.right = right
            # calcultion of css animation rotation out of 100
            self.rightscore = "{0:.0%}".format(right/questionnum)

            # left wing alignment calculation
            leftwing = {"q1":"No", "q2":"Yes", "q3":"No", "q4":"Yes", "q5":"No", "q6":"Yes", "q7":"Yes", "q8":"Yes", "q9":"Yes", "q10":"No", "q11":"No", "q12":"Yes", "q13":"No", "q14":"No", "q15":"Yes", "q16":"No", "q17":"Yes", "q18":"Pro-Choice"}
            # calculate alignment by comparing user input dict to answer key dict
            left_shared = {k: leftwing[k] for k in leftwing if k in d and leftwing[k] == d[k]}
            # number of shared values in dictionary comparison
            left = len(left_shared)
            lefttotal = (left * (-1))
            self.left = left
            # calcultion of css animation rotation out of 100
            self.leftscore = "{0:.0%}".format(left/questionnum)
        
            # independent wing alignment calculation
            indwing = {"q1":"I don't know", "q2":"I don't know", "q3":"I don't know", "q4":"I don't know", "q5":"I don't know", "q6":"I don't know", "q7":"I don't know", "q8":"I don't know", "q9":"I don't know", "q10":"I don't know", "q11":"I don't know", "q12":"I don't know", "q13":"I don't know", "q14":"I don't know", "q15":"I don't know", "q16":"I don't know", "q17":"I don't know", "q18":"I don't know"}
            # calculate alignment by comparing user input dict to answer key dict
            ind_shared = {k: indwing[k] for k in indwing if k in d and indwing[k] == d[k]}
            # number of shared values in dictionary comparison
            ind = len(ind_shared)
            self.ind = ind
            # calcultion of css animation rotation out of 100
            self.indscore = "{0:.0%}".format(ind/questionnum)

            # val alignment calculation
            valwing = {"q1":"I don't know", "q2":"Yes", "q3":"I don't know", "q4":"Yes", "q5":"No", "q6":"Yes", "q7":"Yes", "q8":"Yes", "q9":"Yes", "q10":"Yes", "q11":"I don't know", "q12":"I don't know", "q13":"No", "q14":"I don't know", "q15":"Yes", "q16":"Yes", "q17":"Yes", "q18":"Pro-Choice"}
            # calculate alignment by comparing user input dict to answer key dict
            val_shared = {k: valwing[k] for k in valwing if k in d and valwing[k] == d[k]}
            # number of shared values in dictionary comparison
            valnum = len(val_shared)
            self.valalign = "{0:.0%}".format(valnum/questionnum)
            # calcultion of css animation rotation out of 180
            self.rotateval = (valnum/questionnum) * 180

            # marco alignment calculation
            marcwing = {"q1":"Yes", "q2":"No", "q3":"No", "q4":"No", "q5":"Yes", "q6":"No", "q7":"No", "q8":"No", "q9":"No", "q10":"Yes", "q11":"Yes", "q12":"No", "q13":"Yes", "q14":"Yes", "q15":"No", "q16":"Yes", "q17":"No", "q18":"Pro-Life"}
            # calculate alignment by comparing user input dict to answer key dict
            marc_shared = {k: marcwing[k] for k in marcwing if k in d and marcwing[k] == d[k]}
            # number of shared values in dictionary comparison
            marcnum = len(marc_shared)
            self.marcalign = "{0:.0%}".format(marcnum/questionnum)
            # calcultion of css animation rotation out of 180
            self.rotatemarc = (marcnum/questionnum) * 180

            # ron alignment calculation
            ronwing = {"q1":"Yes", "q2":"No", "q3":"Yes", "q4":"No", "q5":"Yes", "q6":"No", "q7":"No", "q8":"No", "q9":"No", "q10":"Yes", "q11":"Yes", "q12":"No", "q13":"Yes", "q14":"Yes", "q15":"No", "q16":"Yes", "q17":"No", "q18":"Pro-Life"}
            # calculate alignment by comparing user input dict to answer key dict
            ron_shared = {k: ronwing[k] for k in ronwing if k in d and ronwing[k] == d[k]}
            # number of shared values in dictionary comparison
            ronnum = len(ron_shared)
            self.ronalign = "{0:.0%}".format(ronnum/questionnum)
            # calcultion of css animation rotation out of 180
            self.rotateron = (ronnum/questionnum) * 180

            # charlie alignment calculation
            charwing = {"q1":"No", "q2":"Yes", "q3":"No", "q4":"Yes", "q5":"No", "q6":"Yes", "q7":"Yes", "q8":"Yes", "q9":"Yes", "q10":"No", "q11":"No", "q12":"Yes", "q13":"No", "q14":"No", "q15":"Yes", "q16":"No", "q17":"Yes", "q18":"Pro-Choice"}
            # calculate alignment by comparing user input dict to answer key dict
            char_shared = {k: charwing[k] for k in charwing if k in d and charwing[k] == d[k]}
            # number of shared values in dictionary comparison
            charnum = len(char_shared)
            self.charalign = "{0:.0%}".format(charnum/questionnum)
            # calcultion of css animation rotation out of 180
            self.rotatechar = (charnum/questionnum) * 180

        # if no questions were answered
        else:
            # set all variables equal to 0
            self.rightscore = "{0:.0%}".format(0)
            self.leftscore = "{0:.0%}".format(0)
            self.indscore = "{0:.0%}".format(0)
            self.valalign = "{0:.0%}".format(0)
            self.marcalign = "{0:.0%}".format(0)
            self.ronalign = "{0:.0%}".format(0)
            self.charalign = "{0:.0%}".format(0)
            self.totalscore = "{0:.0%}".format(0)
            self.rotatechar = "{0:.0%}".format(0)
            self.rotateval = "{0:.0%}".format(0)
            self.rotateron = "{0:.0%}".format(0)
            self.rotatemarc = "{0:.0%}".format(0)
            
        
    # passing in all values that were calculated
    def __call__(self, rightscore, totalscore, leftscore, indscore, valalign, marcalign, ronalign, charalign, candidates, rotatechar, rotatemarc, rotateval, rotateron, rotatec1, rotatec2, cand1, cand2, cand1score, cand2score, dict1, dict2, dist1, dist2, site1, site2, right, left, ind):
        logging.debug("PrintScore Call Called")
        self.rightscore = rightscore
        self.leftscore = leftscore
        self.indscore = indscore
        self.valalign = valalign
        self.totalscore = totalscore
        self.fmarcalign = marcalign
        self.ronalign = ronalign
        self.charalign = charalign
        self.candidates = candidates
        self.rotatemarc = rotatemarc
        self.rotateval = rotateval
        self.rotateron = rotateron
        self.rotatechar = rotatechar
        self.rotatecand1 = rotatec1
        self.rotatecand2 = rotatec2
        self.cand1 = cand1
        self.cand2 = cand2
        self.cand1score = cand1score
        self.cand2score = cand2score
        self.dict1 = dict1
        self.dict2 = dict2
        self.dist1 = dist1
        self.dist2 = dist2
        self.site1 = site1
        self.site2 = site2
        self.right = right
        self.left = left
        self.ind = ind