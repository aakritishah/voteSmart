from flask_wtf import FlaskForm as Form
from wtforms.validators import InputRequired
from CheckAnswer import CheckAnswer
from wtforms import RadioField
from wtforms.validators import InputRequired

# declaration of questions and answer choices
class PopQuiz(Form):
    class Meta:
        csrf = False

    state = RadioField("What state do you live in?", 
    choices = [("Florida", "Florida")], validators=[InputRequired()])
    
    district = RadioField("Which Florida Disctrict do you reside in?", 
    choices = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"), ("9", "9"), ("10", "10"), ("11", "11"), ("12", "12"), ("13", "13"), ("14", "14"), ("15", "15"), ("16", "16"), ("17", "17"), ("18", "18"), ("19", "19"), ("20", "20"), ("21", "21"), ("22", "22"), ("23", "23"), ("24", "24"), ("25", "25"), ("26", "26"), ("27", "27")], validators=[InputRequired()])

    q1 = RadioField("1. Do you trust the sanctity of United States’ elections?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("Yes")])
    
    q2 = RadioField("2. Do you believe in a person’s right to reproductive freedom?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q3 = RadioField("3. Do you think the existing government is going in the right direction to benefit the people of the country?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("Yes")])

    q4 = RadioField("4. Do you think gun control laws and regulations should be changed?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q5 = RadioField("5. Do you think possession of guns should be allowed to everyone?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("Yes")])

    q6 = RadioField("6. Do you think there should be stricter rules and regulations on the use of money in political campaigns?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q7 = RadioField("7. Should there be policies to resolve the gap between the rich and the poor?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q8 = RadioField("8. Should there be more emphasis on the rehabilitation of criminals than punishment?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q9 = RadioField("9. Should all ethnicities be integrated into society?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q10 = RadioField("10. Have you been a member of the same party your whole life?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("Yes")])

    q11 = RadioField("11. Would you always support your country, whether it was right or wrong?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("Yes")])

    q12 = RadioField("12. Is it foolish to be proud of your country of birth, since no one chooses it?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q13 = RadioField("13. Do you think our race has many superior qualities, compared to other races?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("Yes")])

    q14 = RadioField("14. Is military action that defies international law sometimes justified?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("Yes")])

    q15 = RadioField("15. Do you think that there is a worrying fusion of information and entertainment nowadays?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q16 = RadioField("16. Do you only believe in traditional marriage: i.e. Man and Woman?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q17 = RadioField("17. Do you support the LGBTQ+ community?", 
    choices = [("Yes", "Yes"), ("No", "No"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("No")])

    q18 = RadioField("18. Are your beliefs about women's reproduction more pro-life or more pro-choice?", 
    choices = [("Pro-Life", "Pro-Life"), ("Pro-Choice", "Pro-Choice"), ("I don't know", "I don't know")],
    validators = [CheckAnswer("I don't know")])