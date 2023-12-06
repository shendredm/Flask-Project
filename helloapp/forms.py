from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from markupsafe import Markup
from wtforms import StringField, SubmitField, validators


class QuoteForm(FlaskForm):
    author = StringField(
        "Quote Author",
        validators=[
            validators.DataRequired(message="This field is required"),
            validators.Length(min=3, max=100, message="Field must be between 3 and 200 characters long.")
        ]
    )
    quote = StringField(
        "Quote",
        validators=[
            validators.DataRequired(message="This field is required"),
            validators.Length(min=3, max=200, message="Field must be between 3 and 200 characters long.")
        ]
    )
    submit = SubmitField(" Add Quote")