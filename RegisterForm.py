from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length
from wtforms.validators import InputRequired
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, ValidationError
from User import User

# register form
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Sign-Up")
    # validation of username
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()

        # if username already exists
        if existing_user_username:
            raise ValidationError(
                "That username already exists. Please choose another one."
            )