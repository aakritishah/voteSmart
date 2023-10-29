from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length
from wtforms.validators import InputRequired
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

# location form
class LocationForm(FlaskForm):
    city = StringField(validators=[InputRequired(), Length(min=1, max=50)], render_kw={"placeholder": "City"})
    county = StringField(validators=[InputRequired(), Length(min=1, max=50)], render_kw={"placeholder": "County"})
    state = StringField(validators=[InputRequired(), Length(min=2, max=2)], render_kw={"placeholder": "State (abbreviated)"})
    search = SubmitField("Search Poll Locations")